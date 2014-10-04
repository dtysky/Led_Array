--A program for testing.
--copyright(c) 2014 dtysky

--This program is free software; you can redistribute it and/or modify
--it under the terms of the GNU General Public License as published by
--the Free Software Foundation; either version 2 of the License, or
--(at your option) any later version.

--This program is distributed in the hope that it will be useful,
--but WITHOUT ANY WARRANTY; without even the implied warranty of
--MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
--GNU General Public License for more details.

--You should have received a copy of the GNU General Public License along
--with this program; if not, write to the Free Software Foundation, Inc.,
--51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

------------------------------------------------------------------------
--实现方案：
--由于FIFO输入和输出只能为偶数倍关系，输入又必为32或16bits，所以最后将其调整：
--设立三类FIFO，其中后两类为普通的图片双缓存，第一类为转换

--写入时就按16bits写入！（为了满足要求，由于每一个模块总数据为120*38=4560=285*16），充分利用DM（数据掩码），将RAM作为先后两个RAM对待！
--写入时，一次写入856个16bits数据，丢掉最后一个
--写入时，分为两个1024*16bits的usb数据包，第一个包拥有500*16bits的有效图像数据，第二个有356*16bits，最后一个为随便数据

--读出时，按照16bits读出！顺序写入一个第一类FIFO
--读出时，每张图片第一块总突发次数为125，第二块总突发次数为89（最后一个16bits扔掉）

--第一类FIFO为16bits输入，16bits输出；二三类FIFO为80bits输入，40bis输出
--第一类FIFO和二三类之间插入一个80bits信号做缓存（80=16*5=80*1）
--经计算，每10us需更新一次图片，用此方法，保证FIFO数据流跑到240M（DDR2数据流速度），一次更新只需不到2us，满足要求

--所有输出到RAM的信号初值为0

--再锁定尚待加入

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;

entity LED is
	generic
		(
			constant r20_con:integer:=2047;	------------20r/s时每一度间隔计数（clk_contorl下）
			constant opic_con:integer:=1023;	------------刷一张图片一遍计数
			constant unlock_con:integer:=4095		------------解锁计数
		);
	
	port
		(
			inclk:in std_logic;
			
			data_buffer_a:out std_logic_vector(39 downto 0):=x"0000000000";
			data_buffer_b:out std_logic_vector(39 downto 0):=x"0000000000";
			data_buffer_c:out std_logic_vector(39 downto 0):=x"0000000000";
			en_row_a:out std_logic:='0';
			en_row_b:out std_logic:='0';
			en_row_c:out std_logic_vector(1 downto 0):="00";									--------分割为两个管脚，分配同一信号
			en_col_a_1,en_col_a_2,en_col_a_3:out std_logic:='0';
			en_col_b_1,en_col_b_2,en_col_b_3:out std_logic:='0';
			en_col_c_1,en_col_c_2,en_col_c_3:out std_logic:='0'
		);
end entity;


architecture ledx of LED is

component PLL is
port
	(
		inclk0:in std_logic;
		locked:out std_logic;
		c0:out std_logic
	);
end component;

component IMG1 is
port
(
	clock:in std_logic;
	address:in std_logic_vector(6 downto 0);
	q:out std_logic_vector(39 downto 0)
);
end component;

component IMG2 is
port
(
	clock:in std_logic;
	address:in std_logic_vector(6 downto 0);
	q:out std_logic_vector(39 downto 0)
);
end component;

component IMG3 is
port
(
	clock:in std_logic;
	address:in std_logic_vector(6 downto 0);
	q:out std_logic_vector(39 downto 0)
);
end component;


-------------------图片行-----------------
signal pic_row_ab:bit_vector(37 downto 0):="01111111111111111111111111111111111111";
signal pic_row_c_h:bit_vector(37 downto 0):="01111111111111111111111111111111111111";
signal pic_row_c_l:bit_vector(37 downto 0):="11111111111111111101111111111111111111";

------------------测试用ROM---------------
signal rom_addr:std_logic_vector(6 downto 0):="0000000";
signal rom_clk:std_logic:='0';
signal rom_data1,rom_data2,rom_data3:std_logic_vector(39 downto 0);

--signal test:bit_vector(39 downto 0):=x"0000000001";
signal test_a:bit_vector(39 downto 0):=x"FF00000000";
signal test_b:bit_vector(39 downto 0):=x"0000FF0000";
signal test_c:bit_vector(39 downto 0):=x"00000000FF";

signal clk_self:std_logic;
signal pll_lock:std_logic;


begin

	PLLX:PLL
		port map
			(
				inclk0=>inclk,
				c0=>clk_self,
				locked=>pll_lock
			);
	
	ROM1:IMG1
		port map
			(
				clock=>rom_clk,
				address=>rom_addr,
				q=>rom_data1
			);
			
	ROM2:IMG2
		port map
			(
				clock=>rom_clk,
				address=>rom_addr,
				q=>rom_data2
			);
			
	ROM3:IMG3
		port map
			(
				clock=>rom_clk,
				address=>rom_addr,
				q=>rom_data3
			);

CONTROL:process(clk_self,pll_lock)

variable con_control_work:integer range 0 to 63:=0;

begin

	if clk_self'event and clk_self='1' and pll_lock='1' then
		
		case con_control_work is
		
			when 50 =>
				con_control_work:=0;
			when others =>
				con_control_work:=con_control_work+1;
		
		end case;
			
		case con_control_work is
		
			when 0 =>
				data_buffer_a<=x"0000000000";
				data_buffer_b<=x"0000000000";
				data_buffer_c<=x"0000000000";
				en_row_a<='0';
				en_row_b<='0';
				en_row_c<="00";
			when 1=>
				en_col_a_1<='1';
				en_col_b_1<='1';
				en_col_c_1<='1';
			when 2 =>
				en_col_a_2<='1';
				en_col_b_2<='1';
				en_col_c_2<='1';
			when 3 =>
				en_col_a_3<='1';
				en_col_b_3<='1';
				en_col_c_3<='1';
			when 4 =>
				en_col_a_1<='0';
				en_col_b_1<='0';
				en_col_c_1<='0';
				en_col_a_2<='0';
				en_col_b_2<='0';
				en_col_c_2<='0';
				en_col_a_3<='0';
				en_col_b_3<='0';
				en_col_c_3<='0';
			
			when 5 =>
				data_buffer_a<=x"FFFFFFFFFF";
			when 6 =>
				en_row_a<='1';
			when 7 =>
				en_row_b<='1';
			
			when 8 =>
				data_buffer_c<=x"FFFFFFFFFF";
			when 9 =>
				en_row_c<="11";
			
			when 10 =>
				en_row_a<='0';
				en_row_b<='0';
				en_row_c<="00";
			
			when 12 =>
				data_buffer_a<=x"0000000000";
				data_buffer_c<=x"0000000000";
			
			
			when 15 =>
				rom_clk<='1';
			when 16 =>
				rom_clk<='0';
				rom_addr<=rom_addr+1;
			
			when 17 =>
				data_buffer_a<=rom_data1;
			when 18 =>
				data_buffer_b<=rom_data2;
			when 19 =>
				data_buffer_c<=rom_data3;
			when 20 =>
--				en_col_a_1<='1';
--				en_col_b_1<='1';
--				en_col_c_1<='1';
				en_col_a_3<='1';
				en_col_b_3<='1';
				en_col_c_3<='1';
				
			when 21 =>
				rom_clk<='1';
			when 22 =>
				rom_clk<='0';
				rom_addr<=rom_addr+1;
				
			when 23 =>
				data_buffer_a<=rom_data1;
			when 24 =>
				data_buffer_b<=rom_data2;
			when 25 =>
				data_buffer_c<=rom_data3;
			when 26 =>
--				en_col_a_2<='1';
--				en_col_b_2<='1';
--				en_col_c_2<='1';
				en_col_a_1<='1';
				en_col_b_1<='1';
				en_col_c_1<='1';
			
			when 27 =>
				rom_clk<='1';
			when 28 =>
				rom_clk<='0';
				if rom_addr=113 then
					rom_addr<="0000000";
				else
					rom_addr<=rom_addr+1;
				end if;
			
			when 29 =>
				data_buffer_a<=rom_data1;
			when 30 =>
				data_buffer_b<=rom_data2;
			when 31 =>
				data_buffer_c<=rom_data3;
			when 32 =>
--				en_col_a_3<='1';
--				en_col_b_3<='1';
--				en_col_c_3<='1';
				en_col_a_2<='1';
				en_col_b_2<='1';
				en_col_c_2<='1';
			
			when 33 =>
				data_buffer_a(39 downto 2)<=to_stdlogicvector(pic_row_ab);
			when 34=>
				en_row_a<='1';
			when 35=>
				en_row_b<='1';
			
			when 36 =>
				if pic_row_c_h(37)='0' then
					data_buffer_c(19 downto 1)<="0111111111111111111";
				elsif pic_row_c_h(18)='0' then
					data_buffer_c(19 downto 1)<="1111111111111111111";
				else
					data_buffer_c(19 downto 1)<=to_stdlogicvector(pic_row_c_h(18 downto 0));
				end if;
				
				if pic_row_c_l(0)='0' then
					data_buffer_c(38 downto 20)<="1111111111111111110";
				else
					data_buffer_c(38 downto 20)<=to_stdlogicvector(pic_row_c_l(37 downto 19));
				end if;
			when 37 =>
				en_row_c<="11";
			
			when 50 =>
				pic_row_ab<=pic_row_ab rol 1;
				pic_row_c_h<=pic_row_c_h rol 1;
				pic_row_c_l<=pic_row_c_l ror 1;
				
				--test<=test rol 1;
				--test<= not test; 
				
			when others =>
				null;
				
		end case;
	
	end if;

end process;
			
		
end ledx;
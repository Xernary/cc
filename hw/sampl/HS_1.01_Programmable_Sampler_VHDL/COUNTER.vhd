library IEEE;
use IEEE.std_logic_1164.all;
use ieee.numeric_std.all;

entity COUNTER is
	generic (
		LIMIT : unsigned(31 downto 0) := x"00000064"
	);
	port (
		CLK : in std_logic;
		CLK_EN : in std_logic;
		RST : in std_logic;
		SYNC_RST : in std_logic;
		TC : out std_logic
	);
end COUNTER;

architecture BEHAVIORAL of COUNTER is

	signal COUNT : unsigned(31 downto 0);

begin

	process(CLK, RST)
	begin
		if(RST = '1') then
			COUNT <= (others => '0');
		else
			if(rising_edge(CLK)) then
				if(CLK_EN = '1') then
					if(SYNC_RST = '1') then
						COUNT <= (others => '0');
					else
						if(COUNT = LIMIT) then
							COUNT <= x"00000001";
						else
							COUNT <= COUNT + 1;
						end if; 
					end if;
				end if;
			end if;
		end if;
	end process;

	TC <= '1' when CLK_EN = '1' and COUNT = LIMIT else '0';

end BEHAVIORAL;

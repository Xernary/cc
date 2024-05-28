library IEEE;
use IEEE.std_logic_1164.all;

entity SHIFT_REGISTER is
	generic (
		N : integer := 32
	);
	port (
		CLK : in std_logic;
		RST : in std_logic;
		SYNC_RST : in std_logic;
		SH_IN : in std_logic;
		D_OUT : out std_logic_vector(N-1 downto 0)
	);
end SHIFT_REGISTER;

architecture BEHAVIORAL of SHIFT_REGISTER is

	signal REG : std_logic_vector(N-1 downto 0);

begin

	process(CLK, RST)
	begin
		if(RST = '1') then
			REG <= (others => '0');
		else
			if(rising_edge(CLK)) then
				if(SYNC_RST = '1') then
					REG <= (others => '0');
				else
					REG <= REG(N-2 downto 0) & SH_IN;
				end if;
			end if;
		end if;
	end process;

	D_OUT <= REG;

end BEHAVIORAL;
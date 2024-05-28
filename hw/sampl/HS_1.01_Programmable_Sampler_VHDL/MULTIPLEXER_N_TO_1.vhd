library IEEE;
use IEEE.std_logic_1164.all;
use ieee.numeric_std.all;

entity MULTIPLEXER_N_TO_1 is
	generic (
		N : integer := 32;
		LOGN : integer := 5
	);
	port (
		I : in std_logic_vector(N-1 downto 0);
		SEL : in std_logic_vector(LOGN-1 downto 0);
		O : out std_logic
	);
end MULTIPLEXER_N_TO_1;

architecture BEHAVIORAL of MULTIPLEXER_N_TO_1 is

begin

	O <= I(to_integer(unsigned(SEL)));

end BEHAVIORAL;

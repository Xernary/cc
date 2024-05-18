library IEEE;
use IEEE.std_logic_1164.all;

entity PROGRAMMABLE_SAMPLER_TOP is
	port (
		CLK : in std_logic;
		RST : in std_logic;
		DIN : in std_logic;
		CNTRL : in std_logic_vector(7 downto 0);
		SMPL : out std_logic
	);
end PROGRAMMABLE_SAMPLER_TOP;

architecture STRUCTURAL of PROGRAMMABLE_SAMPLER_TOP is

	signal SHIFT_REGISTER_256_BIT_OUT : std_logic_vector(255 downto 0);
	signal TC_COUNTER_1_MILLION : std_logic;
	signal TC_COUNTER_60_A : std_logic;
	signal TC_COUNTER_60_B : std_logic;

begin

	SHIFT_REGISTER_256_BIT : entity work.SHIFT_REGISTER 
		generic map(
			N => 256
		) 
		port map(
			CLK => CLK, 
			RST => RST, 
			SYNC_RST => TC_COUNTER_60_B, 
			SH_IN => DIN,
			D_OUT => SHIFT_REGISTER_256_BIT_OUT
		);

	MULTIPLEXER_256_TO_1 : entity work.MULTIPLEXER_N_TO_1 
		generic map(
			N => 256,
			LOGN => 8
		) 
		port map(
			I => SHIFT_REGISTER_256_BIT_OUT, 
			SEL => CNTRL, 
			O => SMPL
		);

	COUNTER_1_MILLION : entity work.COUNTER
		generic map(
			LIMIT => x"000F4240"
		) 
		port map(
			CLK => CLK,
			CLK_EN => '1', 
			RST => RST, 
			SYNC_RST => '0', 
			TC => TC_COUNTER_1_MILLION
		);

	COUNTER_60_A : entity work.COUNTER
		generic map(
			LIMIT => x"0000003C"
		) 
		port map(
			CLK => CLK and not(TC_COUNTER_60_A),
			CLK_EN => not(CNTRL(0)), 
			RST => RST, 
			SYNC_RST => CNTRL(0), 
			TC => TC_COUNTER_60_A
		);

	COUNTER_60_B : entity work.COUNTER
		generic map(
			LIMIT => x"0000003C"
		) 
		port map(
			CLK => CLK,
			CLK_EN => TC_COUNTER_1_MILLION and not(TC_COUNTER_60_A), 
			RST => RST, 
			SYNC_RST => '0', 
			TC => TC_COUNTER_60_B
		);

end STRUCTURAL;

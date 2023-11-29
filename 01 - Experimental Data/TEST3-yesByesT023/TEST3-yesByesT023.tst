BEGIN_FILE
	Version 1.0
	Collection CellScaleBiaxial

BEGIN_BLOCK

BEGIN_DEVICES
1	Biotester5000	COM9	AutoDetectCOM	UniAxial	LoadcellX	20000	32.21	Temperature	37	IdleCurrent	1	ThreadsPerInch 6	AllowCompressionTestModes	NoExternalSync
	PreloadEx 2 250 50 600 5 10 100

BEGIN_DISPLAYS
1	Video	1	Live_Video	1084	609	373	337	FixedAspectRatio

BEGIN_CHARTS
1	Force_N	FAuto	0	2	Time_S	FAuto	0	40	Position	600	0
	Series	1	X	(255,0,0)	2
2	Displacement_mm	FAuto	0	30	Time_S	FAuto	0	40	Position	600	350
	Series	1	X	(255,0,0)	2
3	Force_N	FAuto	0	2	Displacement_mm	FAuto	0	30	Position	600	700
	Series	1	X	(255,0,0)	2

BEGIN_HARDWAREOPTS
TemperatureSetPoint	37
PreloadSettingsEx2 2 250 50 600 5 10 10 100
IdleCurrent 1
SyncPulseDivisor -1
TestMode TENSION


BEGIN_CONTROLS
Timestamp	Seconds
SampleSizeX_um	48000
SampleSizeY_um	4700
NumTrueStrainSegments	10
NumDataAveragingPoints	1
SizeAdjustWithPreload
SoftLimits	500	150000	100	40000
SoftForceLimits2	-1	25000
TemperatureWarnings	0	1
ResetWarning	1
ZeroWarning	0
OutputColumns	SetName	Cycle	Time_S	Size_mm	Displacement_mm	Force_N

BEGIN_MULTISET
Name	XMode	XFunction	XUnits	XMagnitude	XPreloadType	XPreloadMag	YMode	YFunction	YUnits	YMagnitude	YPreloadType	YPreloadMag	StretchDurationSec	RecoveryDurationSec	HoldTimeSec	RestTimeSec	NumReps	DataFreqHz	ImageFreqHz	
Tension1	Force	Step	N	120	None	100	Disp	Ramp	um	0	None	100	50	0	0	0	1	5	0	

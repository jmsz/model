

// One layer of the tracker
Volume GeStripDetector
GeStripDetector.Material Germanium
GeStripDetector.Visibility 1 // ????
GeStripDetector.Shape BRIK 10  10  2 // cm


// One Si-Wafer (6x6) of the tracker
//Volume Wafer
//Wafer.Material Silicon
//Wafer.Visibility 1
//#Wafer.LineWidth 3
//Wafer.Color 0
//Wafer.Shape BRIK 3.15 3.15 0.025

// Some plastic around the wafer (Readout-electronics...)
//Volume PCBLong
//PCBLong.Material PCB
//PCBLong.Color 30
//PCBLong.Visibility 0
//PCBLong.Shape BRIK 2.0 11.6 0.025

// Again some plastic around the wafer (Readout-electronics...)
//Volume PCBSmall
//PCBSmall.Material PCB
//PCBSmall.Color 30
//PCBSmall.Visibility 0
//PCBSmall.Shape BRIK 9.6 2.0 0.025

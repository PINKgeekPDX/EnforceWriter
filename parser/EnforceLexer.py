# Generated from EnforceLexer.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,99,721,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,
        97,2,98,7,98,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,
        1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,
        1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,
        1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,
        1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,
        1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,
        1,35,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,
        1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,
        1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,
        1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,
        1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,
        1,45,1,45,1,45,1,45,1,46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,47,
        1,47,1,47,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,
        1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,50,3,50,
        533,8,50,1,51,3,51,536,8,51,1,51,4,51,539,8,51,11,51,12,51,540,1,
        52,3,52,544,8,52,1,52,4,52,547,8,52,11,52,12,52,548,1,52,1,52,5,
        52,553,8,52,10,52,12,52,556,9,52,1,53,1,53,1,53,1,53,5,53,562,8,
        53,10,53,12,53,565,9,53,1,53,1,53,1,54,1,54,1,54,1,54,1,54,1,54,
        1,54,1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,56,
        1,56,1,57,1,57,1,58,1,58,1,59,1,59,1,60,1,60,1,61,1,61,1,62,1,62,
        1,62,1,63,1,63,1,63,1,64,1,64,1,64,1,65,1,65,1,65,1,66,1,66,1,66,
        1,67,1,67,1,67,1,68,1,68,1,68,1,69,1,69,1,69,1,70,1,70,1,70,1,70,
        1,71,1,71,1,71,1,71,1,72,1,72,1,72,1,73,1,73,1,73,1,74,1,74,1,75,
        1,75,1,76,1,76,1,76,1,77,1,77,1,77,1,78,1,78,1,79,1,79,1,80,1,80,
        1,81,1,81,1,82,1,82,1,82,1,83,1,83,1,83,1,84,1,84,1,85,1,85,1,86,
        1,86,1,87,1,87,1,88,1,88,1,89,1,89,1,90,1,90,1,91,1,91,1,92,1,92,
        1,93,1,93,1,94,1,94,1,95,4,95,684,8,95,11,95,12,95,685,1,95,1,95,
        1,96,1,96,1,96,1,96,5,96,694,8,96,10,96,12,96,697,9,96,1,96,1,96,
        1,97,1,97,1,97,1,97,5,97,705,8,97,10,97,12,97,708,9,97,1,97,1,97,
        1,97,1,97,1,97,1,98,1,98,5,98,717,8,98,10,98,12,98,720,9,98,1,706,
        0,99,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,
        13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,
        24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,
        35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,
        46,93,47,95,48,97,49,99,50,101,51,103,52,105,53,107,54,109,55,111,
        56,113,57,115,58,117,59,119,60,121,61,123,62,125,63,127,64,129,65,
        131,66,133,67,135,68,137,69,139,70,141,71,143,72,145,73,147,74,149,
        75,151,76,153,77,155,78,157,79,159,80,161,81,163,82,165,83,167,84,
        169,85,171,86,173,87,175,88,177,89,179,90,181,91,183,92,185,93,187,
        94,189,95,191,96,193,97,195,98,197,99,1,0,6,1,0,48,57,1,0,34,34,
        3,0,9,10,13,13,32,32,2,0,10,10,13,13,3,0,65,90,95,95,97,122,4,0,
        48,57,65,90,95,95,97,122,732,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,
        27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,
        37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,
        47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,
        57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,
        67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,
        77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,
        87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,
        97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,
        0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,
        1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,
        0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,133,1,
        0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,141,1,0,0,0,0,
        143,1,0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,1,0,0,0,0,151,1,0,
        0,0,0,153,1,0,0,0,0,155,1,0,0,0,0,157,1,0,0,0,0,159,1,0,0,0,0,161,
        1,0,0,0,0,163,1,0,0,0,0,165,1,0,0,0,0,167,1,0,0,0,0,169,1,0,0,0,
        0,171,1,0,0,0,0,173,1,0,0,0,0,175,1,0,0,0,0,177,1,0,0,0,0,179,1,
        0,0,0,0,181,1,0,0,0,0,183,1,0,0,0,0,185,1,0,0,0,0,187,1,0,0,0,0,
        189,1,0,0,0,0,191,1,0,0,0,0,193,1,0,0,0,0,195,1,0,0,0,0,197,1,0,
        0,0,1,199,1,0,0,0,3,205,1,0,0,0,5,210,1,0,0,0,7,217,1,0,0,0,9,225,
        1,0,0,0,11,231,1,0,0,0,13,237,1,0,0,0,15,242,1,0,0,0,17,247,1,0,
        0,0,19,251,1,0,0,0,21,260,1,0,0,0,23,268,1,0,0,0,25,271,1,0,0,0,
        27,275,1,0,0,0,29,282,1,0,0,0,31,287,1,0,0,0,33,294,1,0,0,0,35,299,
        1,0,0,0,37,307,1,0,0,0,39,312,1,0,0,0,41,316,1,0,0,0,43,321,1,0,
        0,0,45,329,1,0,0,0,47,334,1,0,0,0,49,341,1,0,0,0,51,350,1,0,0,0,
        53,356,1,0,0,0,55,363,1,0,0,0,57,369,1,0,0,0,59,379,1,0,0,0,61,383,
        1,0,0,0,63,393,1,0,0,0,65,399,1,0,0,0,67,407,1,0,0,0,69,414,1,0,
        0,0,71,423,1,0,0,0,73,430,1,0,0,0,75,436,1,0,0,0,77,442,1,0,0,0,
        79,451,1,0,0,0,81,459,1,0,0,0,83,464,1,0,0,0,85,472,1,0,0,0,87,481,
        1,0,0,0,89,488,1,0,0,0,91,494,1,0,0,0,93,498,1,0,0,0,95,504,1,0,
        0,0,97,509,1,0,0,0,99,516,1,0,0,0,101,532,1,0,0,0,103,535,1,0,0,
        0,105,543,1,0,0,0,107,557,1,0,0,0,109,568,1,0,0,0,111,577,1,0,0,
        0,113,586,1,0,0,0,115,588,1,0,0,0,117,590,1,0,0,0,119,592,1,0,0,
        0,121,594,1,0,0,0,123,596,1,0,0,0,125,598,1,0,0,0,127,601,1,0,0,
        0,129,604,1,0,0,0,131,607,1,0,0,0,133,610,1,0,0,0,135,613,1,0,0,
        0,137,616,1,0,0,0,139,619,1,0,0,0,141,622,1,0,0,0,143,626,1,0,0,
        0,145,630,1,0,0,0,147,633,1,0,0,0,149,636,1,0,0,0,151,638,1,0,0,
        0,153,640,1,0,0,0,155,643,1,0,0,0,157,646,1,0,0,0,159,648,1,0,0,
        0,161,650,1,0,0,0,163,652,1,0,0,0,165,654,1,0,0,0,167,657,1,0,0,
        0,169,660,1,0,0,0,171,662,1,0,0,0,173,664,1,0,0,0,175,666,1,0,0,
        0,177,668,1,0,0,0,179,670,1,0,0,0,181,672,1,0,0,0,183,674,1,0,0,
        0,185,676,1,0,0,0,187,678,1,0,0,0,189,680,1,0,0,0,191,683,1,0,0,
        0,193,689,1,0,0,0,195,700,1,0,0,0,197,714,1,0,0,0,199,200,5,99,0,
        0,200,201,5,108,0,0,201,202,5,97,0,0,202,203,5,115,0,0,203,204,5,
        115,0,0,204,2,1,0,0,0,205,206,5,101,0,0,206,207,5,110,0,0,207,208,
        5,117,0,0,208,209,5,109,0,0,209,4,1,0,0,0,210,211,5,115,0,0,211,
        212,5,119,0,0,212,213,5,105,0,0,213,214,5,116,0,0,214,215,5,99,0,
        0,215,216,5,104,0,0,216,6,1,0,0,0,217,218,5,101,0,0,218,219,5,120,
        0,0,219,220,5,116,0,0,220,221,5,101,0,0,221,222,5,110,0,0,222,223,
        5,100,0,0,223,224,5,115,0,0,224,8,1,0,0,0,225,226,5,99,0,0,226,227,
        5,111,0,0,227,228,5,110,0,0,228,229,5,115,0,0,229,230,5,116,0,0,
        230,10,1,0,0,0,231,232,5,98,0,0,232,233,5,114,0,0,233,234,5,101,
        0,0,234,235,5,97,0,0,235,236,5,107,0,0,236,12,1,0,0,0,237,238,5,
        99,0,0,238,239,5,97,0,0,239,240,5,115,0,0,240,241,5,101,0,0,241,
        14,1,0,0,0,242,243,5,101,0,0,243,244,5,108,0,0,244,245,5,115,0,0,
        245,246,5,101,0,0,246,16,1,0,0,0,247,248,5,102,0,0,248,249,5,111,
        0,0,249,250,5,114,0,0,250,18,1,0,0,0,251,252,5,99,0,0,252,253,5,
        111,0,0,253,254,5,110,0,0,254,255,5,116,0,0,255,256,5,105,0,0,256,
        257,5,110,0,0,257,258,5,117,0,0,258,259,5,101,0,0,259,20,1,0,0,0,
        260,261,5,102,0,0,261,262,5,111,0,0,262,263,5,114,0,0,263,264,5,
        101,0,0,264,265,5,97,0,0,265,266,5,99,0,0,266,267,5,104,0,0,267,
        22,1,0,0,0,268,269,5,105,0,0,269,270,5,102,0,0,270,24,1,0,0,0,271,
        272,5,110,0,0,272,273,5,101,0,0,273,274,5,119,0,0,274,26,1,0,0,0,
        275,276,5,114,0,0,276,277,5,101,0,0,277,278,5,116,0,0,278,279,5,
        117,0,0,279,280,5,114,0,0,280,281,5,110,0,0,281,28,1,0,0,0,282,283,
        5,116,0,0,283,284,5,104,0,0,284,285,5,105,0,0,285,286,5,115,0,0,
        286,30,1,0,0,0,287,288,5,116,0,0,288,289,5,104,0,0,289,290,5,114,
        0,0,290,291,5,101,0,0,291,292,5,97,0,0,292,293,5,100,0,0,293,32,
        1,0,0,0,294,295,5,118,0,0,295,296,5,111,0,0,296,297,5,105,0,0,297,
        298,5,100,0,0,298,34,1,0,0,0,299,300,5,97,0,0,300,301,5,117,0,0,
        301,302,5,116,0,0,302,303,5,111,0,0,303,304,5,112,0,0,304,305,5,
        116,0,0,305,306,5,114,0,0,306,36,1,0,0,0,307,308,5,97,0,0,308,309,
        5,117,0,0,309,310,5,116,0,0,310,311,5,111,0,0,311,38,1,0,0,0,312,
        313,5,114,0,0,313,314,5,101,0,0,314,315,5,102,0,0,315,40,1,0,0,0,
        316,317,5,110,0,0,317,318,5,117,0,0,318,319,5,108,0,0,319,320,5,
        108,0,0,320,42,1,0,0,0,321,322,5,110,0,0,322,323,5,111,0,0,323,324,
        5,116,0,0,324,325,5,110,0,0,325,326,5,117,0,0,326,327,5,108,0,0,
        327,328,5,108,0,0,328,44,1,0,0,0,329,330,5,102,0,0,330,331,5,117,
        0,0,331,332,5,110,0,0,332,333,5,99,0,0,333,46,1,0,0,0,334,335,5,
        110,0,0,335,336,5,97,0,0,336,337,5,116,0,0,337,338,5,105,0,0,338,
        339,5,118,0,0,339,340,5,101,0,0,340,48,1,0,0,0,341,342,5,118,0,0,
        342,343,5,111,0,0,343,344,5,108,0,0,344,345,5,97,0,0,345,346,5,116,
        0,0,346,347,5,105,0,0,347,348,5,108,0,0,348,349,5,101,0,0,349,50,
        1,0,0,0,350,351,5,112,0,0,351,352,5,114,0,0,352,353,5,111,0,0,353,
        354,5,116,0,0,354,355,5,111,0,0,355,52,1,0,0,0,356,357,5,115,0,0,
        357,358,5,116,0,0,358,359,5,97,0,0,359,360,5,116,0,0,360,361,5,105,
        0,0,361,362,5,99,0,0,362,54,1,0,0,0,363,364,5,111,0,0,364,365,5,
        119,0,0,365,366,5,110,0,0,366,367,5,101,0,0,367,368,5,100,0,0,368,
        56,1,0,0,0,369,370,5,114,0,0,370,371,5,101,0,0,371,372,5,102,0,0,
        372,373,5,101,0,0,373,374,5,114,0,0,374,375,5,101,0,0,375,376,5,
        110,0,0,376,377,5,99,0,0,377,378,5,101,0,0,378,58,1,0,0,0,379,380,
        5,111,0,0,380,381,5,117,0,0,381,382,5,116,0,0,382,60,1,0,0,0,383,
        384,5,112,0,0,384,385,5,114,0,0,385,386,5,111,0,0,386,387,5,116,
        0,0,387,388,5,101,0,0,388,389,5,99,0,0,389,390,5,116,0,0,390,391,
        5,101,0,0,391,392,5,100,0,0,392,62,1,0,0,0,393,394,5,101,0,0,394,
        395,5,118,0,0,395,396,5,101,0,0,396,397,5,110,0,0,397,398,5,116,
        0,0,398,64,1,0,0,0,399,400,5,116,0,0,400,401,5,121,0,0,401,402,5,
        112,0,0,402,403,5,101,0,0,403,404,5,100,0,0,404,405,5,101,0,0,405,
        406,5,102,0,0,406,66,1,0,0,0,407,408,5,109,0,0,408,409,5,111,0,0,
        409,410,5,100,0,0,410,411,5,100,0,0,411,412,5,101,0,0,412,413,5,
        100,0,0,413,68,1,0,0,0,414,415,5,111,0,0,415,416,5,118,0,0,416,417,
        5,101,0,0,417,418,5,114,0,0,418,419,5,114,0,0,419,420,5,105,0,0,
        420,421,5,100,0,0,421,422,5,101,0,0,422,70,1,0,0,0,423,424,5,115,
        0,0,424,425,5,101,0,0,425,426,5,97,0,0,426,427,5,108,0,0,427,428,
        5,101,0,0,428,429,5,100,0,0,429,72,1,0,0,0,430,431,5,105,0,0,431,
        432,5,110,0,0,432,433,5,111,0,0,433,434,5,117,0,0,434,435,5,116,
        0,0,435,74,1,0,0,0,436,437,5,115,0,0,437,438,5,117,0,0,438,439,5,
        112,0,0,439,440,5,101,0,0,440,441,5,114,0,0,441,76,1,0,0,0,442,443,
        5,116,0,0,443,444,5,121,0,0,444,445,5,112,0,0,445,446,5,101,0,0,
        446,447,5,110,0,0,447,448,5,97,0,0,448,449,5,109,0,0,449,450,5,101,
        0,0,450,78,1,0,0,0,451,452,5,112,0,0,452,453,5,111,0,0,453,454,5,
        105,0,0,454,455,5,110,0,0,455,456,5,116,0,0,456,457,5,101,0,0,457,
        458,5,114,0,0,458,80,1,0,0,0,459,460,5,103,0,0,460,461,5,111,0,0,
        461,462,5,116,0,0,462,463,5,111,0,0,463,82,1,0,0,0,464,465,5,112,
        0,0,465,466,5,114,0,0,466,467,5,105,0,0,467,468,5,118,0,0,468,469,
        5,97,0,0,469,470,5,116,0,0,470,471,5,101,0,0,471,84,1,0,0,0,472,
        473,5,101,0,0,473,474,5,120,0,0,474,475,5,116,0,0,475,476,5,101,
        0,0,476,477,5,114,0,0,477,478,5,110,0,0,478,479,5,97,0,0,479,480,
        5,108,0,0,480,86,1,0,0,0,481,482,5,100,0,0,482,483,5,101,0,0,483,
        484,5,108,0,0,484,485,5,101,0,0,485,486,5,116,0,0,486,487,5,101,
        0,0,487,88,1,0,0,0,488,489,5,108,0,0,489,490,5,111,0,0,490,491,5,
        99,0,0,491,492,5,97,0,0,492,493,5,108,0,0,493,90,1,0,0,0,494,495,
        5,105,0,0,495,496,5,110,0,0,496,497,5,116,0,0,497,92,1,0,0,0,498,
        499,5,102,0,0,499,500,5,108,0,0,500,501,5,111,0,0,501,502,5,97,0,
        0,502,503,5,116,0,0,503,94,1,0,0,0,504,505,5,98,0,0,505,506,5,111,
        0,0,506,507,5,111,0,0,507,508,5,108,0,0,508,96,1,0,0,0,509,510,5,
        115,0,0,510,511,5,116,0,0,511,512,5,114,0,0,512,513,5,105,0,0,513,
        514,5,110,0,0,514,515,5,103,0,0,515,98,1,0,0,0,516,517,5,118,0,0,
        517,518,5,101,0,0,518,519,5,99,0,0,519,520,5,116,0,0,520,521,5,111,
        0,0,521,522,5,114,0,0,522,100,1,0,0,0,523,524,5,116,0,0,524,525,
        5,114,0,0,525,526,5,117,0,0,526,533,5,101,0,0,527,528,5,102,0,0,
        528,529,5,97,0,0,529,530,5,108,0,0,530,531,5,115,0,0,531,533,5,101,
        0,0,532,523,1,0,0,0,532,527,1,0,0,0,533,102,1,0,0,0,534,536,5,45,
        0,0,535,534,1,0,0,0,535,536,1,0,0,0,536,538,1,0,0,0,537,539,7,0,
        0,0,538,537,1,0,0,0,539,540,1,0,0,0,540,538,1,0,0,0,540,541,1,0,
        0,0,541,104,1,0,0,0,542,544,5,45,0,0,543,542,1,0,0,0,543,544,1,0,
        0,0,544,546,1,0,0,0,545,547,7,0,0,0,546,545,1,0,0,0,547,548,1,0,
        0,0,548,546,1,0,0,0,548,549,1,0,0,0,549,550,1,0,0,0,550,554,5,46,
        0,0,551,553,7,0,0,0,552,551,1,0,0,0,553,556,1,0,0,0,554,552,1,0,
        0,0,554,555,1,0,0,0,555,106,1,0,0,0,556,554,1,0,0,0,557,563,5,34,
        0,0,558,559,5,92,0,0,559,562,5,34,0,0,560,562,8,1,0,0,561,558,1,
        0,0,0,561,560,1,0,0,0,562,565,1,0,0,0,563,561,1,0,0,0,563,564,1,
        0,0,0,564,566,1,0,0,0,565,563,1,0,0,0,566,567,5,34,0,0,567,108,1,
        0,0,0,568,569,5,95,0,0,569,570,5,95,0,0,570,571,5,76,0,0,571,572,
        5,73,0,0,572,573,5,78,0,0,573,574,5,69,0,0,574,575,5,95,0,0,575,
        576,5,95,0,0,576,110,1,0,0,0,577,578,5,95,0,0,578,579,5,95,0,0,579,
        580,5,70,0,0,580,581,5,73,0,0,581,582,5,76,0,0,582,583,5,69,0,0,
        583,584,5,95,0,0,584,585,5,95,0,0,585,112,1,0,0,0,586,587,5,61,0,
        0,587,114,1,0,0,0,588,589,5,43,0,0,589,116,1,0,0,0,590,591,5,45,
        0,0,591,118,1,0,0,0,592,593,5,42,0,0,593,120,1,0,0,0,594,595,5,47,
        0,0,595,122,1,0,0,0,596,597,5,37,0,0,597,124,1,0,0,0,598,599,5,43,
        0,0,599,600,5,43,0,0,600,126,1,0,0,0,601,602,5,45,0,0,602,603,5,
        45,0,0,603,128,1,0,0,0,604,605,5,43,0,0,605,606,5,61,0,0,606,130,
        1,0,0,0,607,608,5,45,0,0,608,609,5,61,0,0,609,132,1,0,0,0,610,611,
        5,42,0,0,611,612,5,61,0,0,612,134,1,0,0,0,613,614,5,47,0,0,614,615,
        5,61,0,0,615,136,1,0,0,0,616,617,5,124,0,0,617,618,5,61,0,0,618,
        138,1,0,0,0,619,620,5,38,0,0,620,621,5,61,0,0,621,140,1,0,0,0,622,
        623,5,60,0,0,623,624,5,60,0,0,624,625,5,61,0,0,625,142,1,0,0,0,626,
        627,5,62,0,0,627,628,5,62,0,0,628,629,5,61,0,0,629,144,1,0,0,0,630,
        631,5,61,0,0,631,632,5,61,0,0,632,146,1,0,0,0,633,634,5,33,0,0,634,
        635,5,61,0,0,635,148,1,0,0,0,636,637,5,60,0,0,637,150,1,0,0,0,638,
        639,5,62,0,0,639,152,1,0,0,0,640,641,5,60,0,0,641,642,5,61,0,0,642,
        154,1,0,0,0,643,644,5,62,0,0,644,645,5,61,0,0,645,156,1,0,0,0,646,
        647,5,124,0,0,647,158,1,0,0,0,648,649,5,38,0,0,649,160,1,0,0,0,650,
        651,5,126,0,0,651,162,1,0,0,0,652,653,5,94,0,0,653,164,1,0,0,0,654,
        655,5,38,0,0,655,656,5,38,0,0,656,166,1,0,0,0,657,658,5,124,0,0,
        658,659,5,124,0,0,659,168,1,0,0,0,660,661,5,33,0,0,661,170,1,0,0,
        0,662,663,5,58,0,0,663,172,1,0,0,0,664,665,5,59,0,0,665,174,1,0,
        0,0,666,667,5,44,0,0,667,176,1,0,0,0,668,669,5,46,0,0,669,178,1,
        0,0,0,670,671,5,40,0,0,671,180,1,0,0,0,672,673,5,41,0,0,673,182,
        1,0,0,0,674,675,5,91,0,0,675,184,1,0,0,0,676,677,5,93,0,0,677,186,
        1,0,0,0,678,679,5,123,0,0,679,188,1,0,0,0,680,681,5,125,0,0,681,
        190,1,0,0,0,682,684,7,2,0,0,683,682,1,0,0,0,684,685,1,0,0,0,685,
        683,1,0,0,0,685,686,1,0,0,0,686,687,1,0,0,0,687,688,6,95,0,0,688,
        192,1,0,0,0,689,690,5,47,0,0,690,691,5,47,0,0,691,695,1,0,0,0,692,
        694,8,3,0,0,693,692,1,0,0,0,694,697,1,0,0,0,695,693,1,0,0,0,695,
        696,1,0,0,0,696,698,1,0,0,0,697,695,1,0,0,0,698,699,6,96,0,0,699,
        194,1,0,0,0,700,701,5,47,0,0,701,702,5,42,0,0,702,706,1,0,0,0,703,
        705,9,0,0,0,704,703,1,0,0,0,705,708,1,0,0,0,706,707,1,0,0,0,706,
        704,1,0,0,0,707,709,1,0,0,0,708,706,1,0,0,0,709,710,5,42,0,0,710,
        711,5,47,0,0,711,712,1,0,0,0,712,713,6,97,0,0,713,196,1,0,0,0,714,
        718,7,4,0,0,715,717,7,5,0,0,716,715,1,0,0,0,717,720,1,0,0,0,718,
        716,1,0,0,0,718,719,1,0,0,0,719,198,1,0,0,0,720,718,1,0,0,0,13,0,
        532,535,540,543,548,554,561,563,685,695,706,718,1,6,0,0
    ]

class EnforceLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CLASS = 1
    ENUM = 2
    SWITCH = 3
    EXTENDS = 4
    CONST = 5
    BREAK = 6
    CASE = 7
    ELSE = 8
    FOR = 9
    CONTINUE = 10
    FOREACH = 11
    IF = 12
    NEW = 13
    RETURN = 14
    THIS = 15
    THREAD = 16
    VOID = 17
    AUTOPTR = 18
    AUTO = 19
    REF = 20
    NULL = 21
    NOTNULL = 22
    FUNC = 23
    NATIVE = 24
    VOLATILE = 25
    PROTO = 26
    STATIC = 27
    OWNED = 28
    REFERENCE = 29
    OUT = 30
    PROTECTED = 31
    EVENT = 32
    TYPEDEF = 33
    MODDED = 34
    OVERRIDE = 35
    SEALED = 36
    INOUT = 37
    SUPER = 38
    TYPENAME = 39
    POINTER = 40
    GOTO = 41
    PRIVATE = 42
    EXTERNAL = 43
    DELETE = 44
    LOCAL = 45
    TYPE_INT = 46
    TYPE_FLOAT = 47
    TYPE_BOOL = 48
    TYPE_STRING = 49
    TYPE_VECTOR = 50
    LiteralBoolean = 51
    LiteralInteger = 52
    LiteralFloat = 53
    LiteralString = 54
    PREPROC_LINE = 55
    PREPROC_FILE = 56
    Assign = 57
    Add = 58
    Subtract = 59
    Multiply = 60
    Divide = 61
    Modulo = 62
    Increment = 63
    Decrement = 64
    Add_Assign = 65
    Subtract_Assign = 66
    Multiply_Assign = 67
    Divide_Assign = 68
    Or_Assign = 69
    And_Assign = 70
    LShift_Assign = 71
    RShift_Assign = 72
    Equal = 73
    Inequal = 74
    Less = 75
    Greater = 76
    LessEqual = 77
    GreaterEqual = 78
    BitwiseOr = 79
    BitwiseAnd = 80
    BitwiseNot = 81
    BitwiseXor = 82
    LogicalAnd = 83
    LogicalOr = 84
    Bang = 85
    Colon = 86
    Semicolon = 87
    Comma = 88
    Dot = 89
    LParenthesis = 90
    RParenthesis = 91
    LSBracket = 92
    RSBracket = 93
    LCurly = 94
    RCurly = 95
    WHITESPACES = 96
    LineComment = 97
    BlockComment = 98
    IDENTIFIER = 99

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'enum'", "'switch'", "'extends'", "'const'", "'break'", 
            "'case'", "'else'", "'for'", "'continue'", "'foreach'", "'if'", 
            "'new'", "'return'", "'this'", "'thread'", "'void'", "'autoptr'", 
            "'auto'", "'ref'", "'null'", "'notnull'", "'func'", "'native'", 
            "'volatile'", "'proto'", "'static'", "'owned'", "'reference'", 
            "'out'", "'protected'", "'event'", "'typedef'", "'modded'", 
            "'override'", "'sealed'", "'inout'", "'super'", "'typename'", 
            "'pointer'", "'goto'", "'private'", "'external'", "'delete'", 
            "'local'", "'int'", "'float'", "'bool'", "'string'", "'vector'", 
            "'__LINE__'", "'__FILE__'", "'='", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'++'", "'--'", "'+='", "'-='", "'*='", "'/='", "'|='", 
            "'&='", "'<<='", "'>>='", "'=='", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'|'", "'&'", "'~'", "'^'", "'&&'", "'||'", "'!'", "':'", 
            "';'", "','", "'.'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "CLASS", "ENUM", "SWITCH", "EXTENDS", "CONST", "BREAK", "CASE", 
            "ELSE", "FOR", "CONTINUE", "FOREACH", "IF", "NEW", "RETURN", 
            "THIS", "THREAD", "VOID", "AUTOPTR", "AUTO", "REF", "NULL", 
            "NOTNULL", "FUNC", "NATIVE", "VOLATILE", "PROTO", "STATIC", 
            "OWNED", "REFERENCE", "OUT", "PROTECTED", "EVENT", "TYPEDEF", 
            "MODDED", "OVERRIDE", "SEALED", "INOUT", "SUPER", "TYPENAME", 
            "POINTER", "GOTO", "PRIVATE", "EXTERNAL", "DELETE", "LOCAL", 
            "TYPE_INT", "TYPE_FLOAT", "TYPE_BOOL", "TYPE_STRING", "TYPE_VECTOR", 
            "LiteralBoolean", "LiteralInteger", "LiteralFloat", "LiteralString", 
            "PREPROC_LINE", "PREPROC_FILE", "Assign", "Add", "Subtract", 
            "Multiply", "Divide", "Modulo", "Increment", "Decrement", "Add_Assign", 
            "Subtract_Assign", "Multiply_Assign", "Divide_Assign", "Or_Assign", 
            "And_Assign", "LShift_Assign", "RShift_Assign", "Equal", "Inequal", 
            "Less", "Greater", "LessEqual", "GreaterEqual", "BitwiseOr", 
            "BitwiseAnd", "BitwiseNot", "BitwiseXor", "LogicalAnd", "LogicalOr", 
            "Bang", "Colon", "Semicolon", "Comma", "Dot", "LParenthesis", 
            "RParenthesis", "LSBracket", "RSBracket", "LCurly", "RCurly", 
            "WHITESPACES", "LineComment", "BlockComment", "IDENTIFIER" ]

    ruleNames = [ "CLASS", "ENUM", "SWITCH", "EXTENDS", "CONST", "BREAK", 
                  "CASE", "ELSE", "FOR", "CONTINUE", "FOREACH", "IF", "NEW", 
                  "RETURN", "THIS", "THREAD", "VOID", "AUTOPTR", "AUTO", 
                  "REF", "NULL", "NOTNULL", "FUNC", "NATIVE", "VOLATILE", 
                  "PROTO", "STATIC", "OWNED", "REFERENCE", "OUT", "PROTECTED", 
                  "EVENT", "TYPEDEF", "MODDED", "OVERRIDE", "SEALED", "INOUT", 
                  "SUPER", "TYPENAME", "POINTER", "GOTO", "PRIVATE", "EXTERNAL", 
                  "DELETE", "LOCAL", "TYPE_INT", "TYPE_FLOAT", "TYPE_BOOL", 
                  "TYPE_STRING", "TYPE_VECTOR", "LiteralBoolean", "LiteralInteger", 
                  "LiteralFloat", "LiteralString", "PREPROC_LINE", "PREPROC_FILE", 
                  "Assign", "Add", "Subtract", "Multiply", "Divide", "Modulo", 
                  "Increment", "Decrement", "Add_Assign", "Subtract_Assign", 
                  "Multiply_Assign", "Divide_Assign", "Or_Assign", "And_Assign", 
                  "LShift_Assign", "RShift_Assign", "Equal", "Inequal", 
                  "Less", "Greater", "LessEqual", "GreaterEqual", "BitwiseOr", 
                  "BitwiseAnd", "BitwiseNot", "BitwiseXor", "LogicalAnd", 
                  "LogicalOr", "Bang", "Colon", "Semicolon", "Comma", "Dot", 
                  "LParenthesis", "RParenthesis", "LSBracket", "RSBracket", 
                  "LCurly", "RCurly", "WHITESPACES", "LineComment", "BlockComment", 
                  "IDENTIFIER" ]

    grammarFileName = "EnforceLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


# Generated from EnforceParser.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,101,716,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,
        46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,
        52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,
        59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,
        65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,1,0,1,0,5,0,143,8,0,10,
        0,12,0,146,9,0,1,0,1,0,1,1,1,1,3,1,152,8,1,1,2,1,2,1,2,3,2,157,8,
        2,1,3,1,3,1,3,5,3,162,8,3,10,3,12,3,165,9,3,1,3,3,3,168,8,3,1,4,
        3,4,171,8,4,1,4,5,4,174,8,4,10,4,12,4,177,9,4,1,4,1,4,1,4,1,4,1,
        5,1,5,1,5,5,5,186,8,5,10,5,12,5,189,9,5,1,6,1,6,1,6,3,6,194,8,6,
        1,6,3,6,197,8,6,1,6,1,6,3,6,201,8,6,1,7,3,7,204,8,7,1,7,5,7,207,
        8,7,10,7,12,7,210,9,7,1,7,1,7,1,7,3,7,215,8,7,1,7,3,7,218,8,7,1,
        7,1,7,1,7,3,7,223,8,7,1,7,3,7,226,8,7,1,8,1,8,1,8,1,8,5,8,232,8,
        8,10,8,12,8,235,9,8,3,8,237,8,8,1,8,1,8,1,9,5,9,242,8,9,10,9,12,
        9,245,9,9,1,9,1,9,1,9,1,10,3,10,251,8,10,1,10,5,10,254,8,10,10,10,
        12,10,257,9,10,1,10,1,10,1,10,3,10,262,8,10,1,10,3,10,265,8,10,1,
        10,3,10,268,8,10,1,10,3,10,271,8,10,1,11,3,11,274,8,11,1,11,5,11,
        277,8,11,10,11,12,11,280,9,11,1,11,1,11,1,11,3,11,285,8,11,1,11,
        1,11,3,11,289,8,11,1,12,1,12,1,12,1,12,5,12,295,8,12,10,12,12,12,
        298,9,12,3,12,300,8,12,1,12,3,12,303,8,12,1,12,3,12,306,8,12,1,12,
        1,12,3,12,310,8,12,1,13,1,13,1,13,3,13,315,8,13,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,3,14,325,8,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,3,14,360,8,14,1,14,1,14,1,14,1,14,5,14,366,8,14,10,14,12,
        14,369,9,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,3,16,386,8,16,1,17,1,17,5,17,390,8,17,10,
        17,12,17,393,9,17,1,17,1,17,3,17,397,8,17,1,17,3,17,400,8,17,1,18,
        1,18,1,18,1,18,3,18,406,8,18,1,18,3,18,409,8,18,1,19,1,19,1,19,1,
        19,1,20,1,20,3,20,417,8,20,1,20,1,20,1,21,1,21,1,21,5,21,424,8,21,
        10,21,12,21,427,9,21,1,22,1,22,3,22,431,8,22,1,23,1,23,1,23,1,23,
        1,24,1,24,1,25,1,25,1,25,5,25,442,8,25,10,25,12,25,445,9,25,1,25,
        3,25,448,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,470,8,26,
        1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,3,29,483,
        8,29,1,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,
        1,33,1,33,1,33,1,33,1,33,5,33,502,8,33,10,33,12,33,505,9,33,1,33,
        1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,5,35,
        520,8,35,10,35,12,35,523,9,35,1,35,1,35,1,36,1,36,3,36,529,8,36,
        1,36,1,36,1,37,1,37,1,37,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,
        1,40,1,40,1,40,1,40,3,40,548,8,40,1,40,5,40,551,8,40,10,40,12,40,
        554,9,40,1,41,1,41,1,41,1,42,1,42,1,43,1,43,1,43,5,43,564,8,43,10,
        43,12,43,567,9,43,1,43,5,43,570,8,43,10,43,12,43,573,9,43,1,44,1,
        44,3,44,577,8,44,1,44,1,44,1,45,1,45,3,45,583,8,45,1,45,1,45,1,46,
        1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,51,5,51,598,8,51,
        10,51,12,51,601,9,51,1,51,1,51,1,51,1,52,1,52,1,52,1,52,5,52,610,
        8,52,10,52,12,52,613,9,52,1,52,3,52,616,8,52,1,53,1,53,1,53,5,53,
        621,8,53,10,53,12,53,624,9,53,1,53,3,53,627,8,53,1,54,1,54,3,54,
        631,8,54,1,55,1,55,1,55,1,56,3,56,637,8,56,1,56,1,56,1,56,1,56,3,
        56,643,8,56,1,56,1,56,1,56,1,57,1,57,3,57,650,8,57,1,58,1,58,1,59,
        1,59,1,59,1,59,5,59,658,8,59,10,59,12,59,661,9,59,1,59,1,59,1,60,
        5,60,666,8,60,10,60,12,60,669,9,60,1,60,1,60,1,61,1,61,1,61,1,61,
        5,61,677,8,61,10,61,12,61,680,9,61,1,61,1,61,1,62,5,62,685,8,62,
        10,62,12,62,688,9,62,1,62,1,62,1,62,1,62,3,62,694,8,62,1,63,1,63,
        1,63,1,63,1,64,1,64,3,64,702,8,64,1,65,1,65,1,65,1,66,1,66,1,66,
        1,67,1,67,1,68,1,68,1,69,1,69,1,69,0,1,28,70,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,
        134,136,138,0,17,2,0,87,88,96,96,4,0,58,59,63,64,81,81,85,85,1,0,
        60,62,1,0,58,59,1,0,75,78,1,0,73,74,1,0,79,82,1,0,83,84,2,0,57,57,
        65,72,1,0,63,64,2,0,4,4,86,86,6,0,17,17,19,19,23,23,39,39,46,50,
        99,99,1,0,54,56,2,0,1,51,101,101,2,0,34,34,36,36,8,0,5,5,18,18,20,
        20,22,22,26,31,37,37,42,42,45,45,5,0,20,20,24,29,31,32,35,35,42,
        43,760,0,144,1,0,0,0,2,151,1,0,0,0,4,156,1,0,0,0,6,167,1,0,0,0,8,
        170,1,0,0,0,10,182,1,0,0,0,12,190,1,0,0,0,14,203,1,0,0,0,16,227,
        1,0,0,0,18,243,1,0,0,0,20,250,1,0,0,0,22,273,1,0,0,0,24,290,1,0,
        0,0,26,311,1,0,0,0,28,324,1,0,0,0,30,370,1,0,0,0,32,385,1,0,0,0,
        34,387,1,0,0,0,36,401,1,0,0,0,38,410,1,0,0,0,40,414,1,0,0,0,42,420,
        1,0,0,0,44,430,1,0,0,0,46,432,1,0,0,0,48,436,1,0,0,0,50,447,1,0,
        0,0,52,469,1,0,0,0,54,471,1,0,0,0,56,474,1,0,0,0,58,478,1,0,0,0,
        60,484,1,0,0,0,62,487,1,0,0,0,64,490,1,0,0,0,66,496,1,0,0,0,68,511,
        1,0,0,0,70,515,1,0,0,0,72,526,1,0,0,0,74,532,1,0,0,0,76,535,1,0,
        0,0,78,538,1,0,0,0,80,543,1,0,0,0,82,555,1,0,0,0,84,558,1,0,0,0,
        86,560,1,0,0,0,88,574,1,0,0,0,90,580,1,0,0,0,92,586,1,0,0,0,94,588,
        1,0,0,0,96,590,1,0,0,0,98,592,1,0,0,0,100,594,1,0,0,0,102,599,1,
        0,0,0,104,605,1,0,0,0,106,617,1,0,0,0,108,630,1,0,0,0,110,632,1,
        0,0,0,112,636,1,0,0,0,114,649,1,0,0,0,116,651,1,0,0,0,118,653,1,
        0,0,0,120,667,1,0,0,0,122,672,1,0,0,0,124,686,1,0,0,0,126,695,1,
        0,0,0,128,699,1,0,0,0,130,703,1,0,0,0,132,706,1,0,0,0,134,709,1,
        0,0,0,136,711,1,0,0,0,138,713,1,0,0,0,140,143,3,2,1,0,141,143,3,
        4,2,0,142,140,1,0,0,0,142,141,1,0,0,0,143,146,1,0,0,0,144,142,1,
        0,0,0,144,145,1,0,0,0,145,147,1,0,0,0,146,144,1,0,0,0,147,148,5,
        0,0,1,148,1,1,0,0,0,149,152,3,8,4,0,150,152,3,14,7,0,151,149,1,0,
        0,0,151,150,1,0,0,0,152,3,1,0,0,0,153,157,3,20,10,0,154,157,3,22,
        11,0,155,157,3,112,56,0,156,153,1,0,0,0,156,154,1,0,0,0,156,155,
        1,0,0,0,157,5,1,0,0,0,158,168,3,2,1,0,159,163,5,94,0,0,160,162,3,
        2,1,0,161,160,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,
        0,0,0,164,166,1,0,0,0,165,163,1,0,0,0,166,168,5,95,0,0,167,158,1,
        0,0,0,167,159,1,0,0,0,168,7,1,0,0,0,169,171,3,126,63,0,170,169,1,
        0,0,0,170,171,1,0,0,0,171,175,1,0,0,0,172,174,3,136,68,0,173,172,
        1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,178,
        1,0,0,0,177,175,1,0,0,0,178,179,3,128,64,0,179,180,3,10,5,0,180,
        181,5,87,0,0,181,9,1,0,0,0,182,187,3,12,6,0,183,184,5,88,0,0,184,
        186,3,12,6,0,185,183,1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,
        188,1,0,0,0,188,11,1,0,0,0,189,187,1,0,0,0,190,196,3,84,42,0,191,
        193,5,92,0,0,192,194,3,28,14,0,193,192,1,0,0,0,193,194,1,0,0,0,194,
        195,1,0,0,0,195,197,5,93,0,0,196,191,1,0,0,0,196,197,1,0,0,0,197,
        200,1,0,0,0,198,199,5,57,0,0,199,201,3,28,14,0,200,198,1,0,0,0,200,
        201,1,0,0,0,201,13,1,0,0,0,202,204,3,126,63,0,203,202,1,0,0,0,203,
        204,1,0,0,0,204,208,1,0,0,0,205,207,3,138,69,0,206,205,1,0,0,0,207,
        210,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,211,1,0,0,0,210,
        208,1,0,0,0,211,214,3,128,64,0,212,213,5,92,0,0,213,215,5,93,0,0,
        214,212,1,0,0,0,214,215,1,0,0,0,215,217,1,0,0,0,216,218,5,81,0,0,
        217,216,1,0,0,0,217,218,1,0,0,0,218,219,1,0,0,0,219,220,3,84,42,
        0,220,222,3,16,8,0,221,223,3,48,24,0,222,221,1,0,0,0,222,223,1,0,
        0,0,223,225,1,0,0,0,224,226,5,87,0,0,225,224,1,0,0,0,225,226,1,0,
        0,0,226,15,1,0,0,0,227,236,5,90,0,0,228,233,3,18,9,0,229,230,5,88,
        0,0,230,232,3,18,9,0,231,229,1,0,0,0,232,235,1,0,0,0,233,231,1,0,
        0,0,233,234,1,0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,236,228,1,0,
        0,0,236,237,1,0,0,0,237,238,1,0,0,0,238,239,5,91,0,0,239,17,1,0,
        0,0,240,242,3,136,68,0,241,240,1,0,0,0,242,245,1,0,0,0,243,241,1,
        0,0,0,243,244,1,0,0,0,244,246,1,0,0,0,245,243,1,0,0,0,246,247,3,
        128,64,0,247,248,3,12,6,0,248,19,1,0,0,0,249,251,3,126,63,0,250,
        249,1,0,0,0,250,251,1,0,0,0,251,255,1,0,0,0,252,254,3,134,67,0,253,
        252,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,256,
        258,1,0,0,0,257,255,1,0,0,0,258,259,5,1,0,0,259,261,3,84,42,0,260,
        262,3,122,61,0,261,260,1,0,0,0,261,262,1,0,0,0,262,264,1,0,0,0,263,
        265,3,82,41,0,264,263,1,0,0,0,264,265,1,0,0,0,265,267,1,0,0,0,266,
        268,3,6,3,0,267,266,1,0,0,0,267,268,1,0,0,0,268,270,1,0,0,0,269,
        271,5,87,0,0,270,269,1,0,0,0,270,271,1,0,0,0,271,21,1,0,0,0,272,
        274,3,126,63,0,273,272,1,0,0,0,273,274,1,0,0,0,274,278,1,0,0,0,275,
        277,3,134,67,0,276,275,1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,
        279,1,0,0,0,279,281,1,0,0,0,280,278,1,0,0,0,281,282,5,2,0,0,282,
        284,3,84,42,0,283,285,3,82,41,0,284,283,1,0,0,0,284,285,1,0,0,0,
        285,286,1,0,0,0,286,288,3,24,12,0,287,289,5,87,0,0,288,287,1,0,0,
        0,288,289,1,0,0,0,289,23,1,0,0,0,290,299,5,94,0,0,291,296,3,26,13,
        0,292,293,7,0,0,0,293,295,3,26,13,0,294,292,1,0,0,0,295,298,1,0,
        0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,300,1,0,0,0,298,296,1,0,
        0,0,299,291,1,0,0,0,299,300,1,0,0,0,300,302,1,0,0,0,301,303,5,88,
        0,0,302,301,1,0,0,0,302,303,1,0,0,0,303,305,1,0,0,0,304,306,5,87,
        0,0,305,304,1,0,0,0,305,306,1,0,0,0,306,307,1,0,0,0,307,309,5,95,
        0,0,308,310,5,87,0,0,309,308,1,0,0,0,309,310,1,0,0,0,310,25,1,0,
        0,0,311,314,3,84,42,0,312,313,5,57,0,0,313,315,3,28,14,0,314,312,
        1,0,0,0,314,315,1,0,0,0,315,27,1,0,0,0,316,317,6,14,-1,0,317,325,
        3,32,16,0,318,325,5,15,0,0,319,325,5,38,0,0,320,325,3,34,17,0,321,
        325,3,30,15,0,322,323,7,1,0,0,323,325,3,28,14,10,324,316,1,0,0,0,
        324,318,1,0,0,0,324,319,1,0,0,0,324,320,1,0,0,0,324,321,1,0,0,0,
        324,322,1,0,0,0,325,367,1,0,0,0,326,327,10,9,0,0,327,328,7,2,0,0,
        328,366,3,28,14,10,329,330,10,8,0,0,330,331,7,3,0,0,331,366,3,28,
        14,9,332,333,10,7,0,0,333,334,3,132,66,0,334,335,3,28,14,8,335,366,
        1,0,0,0,336,337,10,6,0,0,337,338,3,130,65,0,338,339,3,28,14,7,339,
        366,1,0,0,0,340,341,10,5,0,0,341,342,7,4,0,0,342,366,3,28,14,6,343,
        344,10,4,0,0,344,345,7,5,0,0,345,366,3,28,14,5,346,347,10,3,0,0,
        347,348,7,6,0,0,348,366,3,28,14,4,349,350,10,2,0,0,350,351,7,7,0,
        0,351,366,3,28,14,3,352,353,10,1,0,0,353,354,7,8,0,0,354,366,3,28,
        14,1,355,356,10,15,0,0,356,359,5,89,0,0,357,360,3,84,42,0,358,360,
        3,36,18,0,359,357,1,0,0,0,359,358,1,0,0,0,360,366,1,0,0,0,361,362,
        10,12,0,0,362,366,3,88,44,0,363,364,10,11,0,0,364,366,7,9,0,0,365,
        326,1,0,0,0,365,329,1,0,0,0,365,332,1,0,0,0,365,336,1,0,0,0,365,
        340,1,0,0,0,365,343,1,0,0,0,365,346,1,0,0,0,365,349,1,0,0,0,365,
        352,1,0,0,0,365,355,1,0,0,0,365,361,1,0,0,0,365,363,1,0,0,0,366,
        369,1,0,0,0,367,365,1,0,0,0,367,368,1,0,0,0,368,29,1,0,0,0,369,367,
        1,0,0,0,370,371,5,90,0,0,371,372,3,128,64,0,372,373,5,91,0,0,373,
        374,3,28,14,0,374,31,1,0,0,0,375,386,3,36,18,0,376,386,3,92,46,0,
        377,386,3,94,47,0,378,386,3,98,49,0,379,386,3,100,50,0,380,386,3,
        38,19,0,381,386,3,90,45,0,382,386,3,96,48,0,383,386,3,84,42,0,384,
        386,3,128,64,0,385,375,1,0,0,0,385,376,1,0,0,0,385,377,1,0,0,0,385,
        378,1,0,0,0,385,379,1,0,0,0,385,380,1,0,0,0,385,381,1,0,0,0,385,
        382,1,0,0,0,385,383,1,0,0,0,385,384,1,0,0,0,386,33,1,0,0,0,387,391,
        5,13,0,0,388,390,3,136,68,0,389,388,1,0,0,0,390,393,1,0,0,0,391,
        389,1,0,0,0,391,392,1,0,0,0,392,394,1,0,0,0,393,391,1,0,0,0,394,
        396,3,84,42,0,395,397,3,118,59,0,396,395,1,0,0,0,396,397,1,0,0,0,
        397,399,1,0,0,0,398,400,3,40,20,0,399,398,1,0,0,0,399,400,1,0,0,
        0,400,35,1,0,0,0,401,402,3,84,42,0,402,408,3,40,20,0,403,405,5,92,
        0,0,404,406,3,28,14,0,405,404,1,0,0,0,405,406,1,0,0,0,406,407,1,
        0,0,0,407,409,5,93,0,0,408,403,1,0,0,0,408,409,1,0,0,0,409,37,1,
        0,0,0,410,411,5,90,0,0,411,412,3,28,14,0,412,413,5,91,0,0,413,39,
        1,0,0,0,414,416,5,90,0,0,415,417,3,42,21,0,416,415,1,0,0,0,416,417,
        1,0,0,0,417,418,1,0,0,0,418,419,5,91,0,0,419,41,1,0,0,0,420,425,
        3,44,22,0,421,422,5,88,0,0,422,424,3,44,22,0,423,421,1,0,0,0,424,
        427,1,0,0,0,425,423,1,0,0,0,425,426,1,0,0,0,426,43,1,0,0,0,427,425,
        1,0,0,0,428,431,3,28,14,0,429,431,3,46,23,0,430,428,1,0,0,0,430,
        429,1,0,0,0,431,45,1,0,0,0,432,433,3,84,42,0,433,434,5,86,0,0,434,
        435,3,28,14,0,435,47,1,0,0,0,436,437,3,52,26,0,437,49,1,0,0,0,438,
        448,3,110,55,0,439,443,5,94,0,0,440,442,3,52,26,0,441,440,1,0,0,
        0,442,445,1,0,0,0,443,441,1,0,0,0,443,444,1,0,0,0,444,446,1,0,0,
        0,445,443,1,0,0,0,446,448,5,95,0,0,447,438,1,0,0,0,447,439,1,0,0,
        0,448,51,1,0,0,0,449,450,3,28,14,0,450,451,5,87,0,0,451,470,1,0,
        0,0,452,470,3,8,4,0,453,454,3,62,31,0,454,455,5,87,0,0,455,470,1,
        0,0,0,456,470,3,58,29,0,457,470,3,64,32,0,458,470,3,66,33,0,459,
        470,3,68,34,0,460,470,3,70,35,0,461,470,3,72,36,0,462,470,3,74,37,
        0,463,470,3,76,38,0,464,470,3,50,25,0,465,470,3,56,28,0,466,470,
        3,78,39,0,467,470,3,54,27,0,468,470,5,87,0,0,469,449,1,0,0,0,469,
        452,1,0,0,0,469,453,1,0,0,0,469,456,1,0,0,0,469,457,1,0,0,0,469,
        458,1,0,0,0,469,459,1,0,0,0,469,460,1,0,0,0,469,461,1,0,0,0,469,
        462,1,0,0,0,469,463,1,0,0,0,469,464,1,0,0,0,469,465,1,0,0,0,469,
        466,1,0,0,0,469,467,1,0,0,0,469,468,1,0,0,0,470,53,1,0,0,0,471,472,
        5,16,0,0,472,473,3,36,18,0,473,55,1,0,0,0,474,475,5,41,0,0,475,476,
        3,28,14,0,476,477,5,87,0,0,477,57,1,0,0,0,478,479,5,12,0,0,479,480,
        3,38,19,0,480,482,3,48,24,0,481,483,3,60,30,0,482,481,1,0,0,0,482,
        483,1,0,0,0,483,59,1,0,0,0,484,485,5,8,0,0,485,486,3,48,24,0,486,
        61,1,0,0,0,487,488,5,44,0,0,488,489,3,28,14,0,489,63,1,0,0,0,490,
        491,5,9,0,0,491,492,5,90,0,0,492,493,3,80,40,0,493,494,5,91,0,0,
        494,495,3,48,24,0,495,65,1,0,0,0,496,497,5,11,0,0,497,498,5,90,0,
        0,498,503,3,102,51,0,499,500,5,88,0,0,500,502,3,102,51,0,501,499,
        1,0,0,0,502,505,1,0,0,0,503,501,1,0,0,0,503,504,1,0,0,0,504,506,
        1,0,0,0,505,503,1,0,0,0,506,507,5,86,0,0,507,508,3,28,14,0,508,509,
        5,91,0,0,509,510,3,48,24,0,510,67,1,0,0,0,511,512,5,100,0,0,512,
        513,3,38,19,0,513,514,3,48,24,0,514,69,1,0,0,0,515,516,5,3,0,0,516,
        517,3,38,19,0,517,521,5,94,0,0,518,520,3,108,54,0,519,518,1,0,0,
        0,520,523,1,0,0,0,521,519,1,0,0,0,521,522,1,0,0,0,522,524,1,0,0,
        0,523,521,1,0,0,0,524,525,5,95,0,0,525,71,1,0,0,0,526,528,5,14,0,
        0,527,529,3,28,14,0,528,527,1,0,0,0,528,529,1,0,0,0,529,530,1,0,
        0,0,530,531,5,87,0,0,531,73,1,0,0,0,532,533,5,6,0,0,533,534,5,87,
        0,0,534,75,1,0,0,0,535,536,5,10,0,0,536,537,5,87,0,0,537,77,1,0,
        0,0,538,539,3,128,64,0,539,540,3,84,42,0,540,541,3,40,20,0,541,542,
        5,87,0,0,542,79,1,0,0,0,543,544,3,52,26,0,544,545,3,28,14,0,545,
        547,5,87,0,0,546,548,3,28,14,0,547,546,1,0,0,0,547,548,1,0,0,0,548,
        552,1,0,0,0,549,551,5,87,0,0,550,549,1,0,0,0,551,554,1,0,0,0,552,
        550,1,0,0,0,552,553,1,0,0,0,553,81,1,0,0,0,554,552,1,0,0,0,555,556,
        7,10,0,0,556,557,3,128,64,0,557,83,1,0,0,0,558,559,7,11,0,0,559,
        85,1,0,0,0,560,565,3,28,14,0,561,562,5,88,0,0,562,564,3,28,14,0,
        563,561,1,0,0,0,564,567,1,0,0,0,565,563,1,0,0,0,565,566,1,0,0,0,
        566,571,1,0,0,0,567,565,1,0,0,0,568,570,5,88,0,0,569,568,1,0,0,0,
        570,573,1,0,0,0,571,569,1,0,0,0,571,572,1,0,0,0,572,87,1,0,0,0,573,
        571,1,0,0,0,574,576,5,92,0,0,575,577,3,28,14,0,576,575,1,0,0,0,576,
        577,1,0,0,0,577,578,1,0,0,0,578,579,5,93,0,0,579,89,1,0,0,0,580,
        582,5,94,0,0,581,583,3,86,43,0,582,581,1,0,0,0,582,583,1,0,0,0,583,
        584,1,0,0,0,584,585,5,95,0,0,585,91,1,0,0,0,586,587,7,12,0,0,587,
        93,1,0,0,0,588,589,5,52,0,0,589,95,1,0,0,0,590,591,5,21,0,0,591,
        97,1,0,0,0,592,593,5,53,0,0,593,99,1,0,0,0,594,595,5,51,0,0,595,
        101,1,0,0,0,596,598,3,136,68,0,597,596,1,0,0,0,598,601,1,0,0,0,599,
        597,1,0,0,0,599,600,1,0,0,0,600,602,1,0,0,0,601,599,1,0,0,0,602,
        603,3,128,64,0,603,604,3,84,42,0,604,103,1,0,0,0,605,606,5,7,0,0,
        606,607,3,28,14,0,607,615,5,86,0,0,608,610,3,52,26,0,609,608,1,0,
        0,0,610,613,1,0,0,0,611,609,1,0,0,0,611,612,1,0,0,0,612,616,1,0,
        0,0,613,611,1,0,0,0,614,616,3,48,24,0,615,611,1,0,0,0,615,614,1,
        0,0,0,616,105,1,0,0,0,617,618,5,101,0,0,618,626,5,86,0,0,619,621,
        3,52,26,0,620,619,1,0,0,0,621,624,1,0,0,0,622,620,1,0,0,0,622,623,
        1,0,0,0,623,627,1,0,0,0,624,622,1,0,0,0,625,627,3,48,24,0,626,622,
        1,0,0,0,626,625,1,0,0,0,627,107,1,0,0,0,628,631,3,104,52,0,629,631,
        3,106,53,0,630,628,1,0,0,0,630,629,1,0,0,0,631,109,1,0,0,0,632,633,
        5,94,0,0,633,634,5,95,0,0,634,111,1,0,0,0,635,637,3,126,63,0,636,
        635,1,0,0,0,636,637,1,0,0,0,637,638,1,0,0,0,638,639,5,33,0,0,639,
        642,3,114,57,0,640,641,5,92,0,0,641,643,5,93,0,0,642,640,1,0,0,0,
        642,643,1,0,0,0,643,644,1,0,0,0,644,645,3,84,42,0,645,646,5,87,0,
        0,646,113,1,0,0,0,647,650,3,116,58,0,648,650,3,128,64,0,649,647,
        1,0,0,0,649,648,1,0,0,0,650,115,1,0,0,0,651,652,7,13,0,0,652,117,
        1,0,0,0,653,654,5,75,0,0,654,659,3,120,60,0,655,656,5,88,0,0,656,
        658,3,120,60,0,657,655,1,0,0,0,658,661,1,0,0,0,659,657,1,0,0,0,659,
        660,1,0,0,0,660,662,1,0,0,0,661,659,1,0,0,0,662,663,5,76,0,0,663,
        119,1,0,0,0,664,666,3,136,68,0,665,664,1,0,0,0,666,669,1,0,0,0,667,
        665,1,0,0,0,667,668,1,0,0,0,668,670,1,0,0,0,669,667,1,0,0,0,670,
        671,3,128,64,0,671,121,1,0,0,0,672,673,5,75,0,0,673,678,3,124,62,
        0,674,675,5,88,0,0,675,677,3,124,62,0,676,674,1,0,0,0,677,680,1,
        0,0,0,678,676,1,0,0,0,678,679,1,0,0,0,679,681,1,0,0,0,680,678,1,
        0,0,0,681,682,5,76,0,0,682,123,1,0,0,0,683,685,3,136,68,0,684,683,
        1,0,0,0,685,688,1,0,0,0,686,684,1,0,0,0,686,687,1,0,0,0,687,689,
        1,0,0,0,688,686,1,0,0,0,689,690,3,128,64,0,690,693,3,84,42,0,691,
        692,5,92,0,0,692,694,5,93,0,0,693,691,1,0,0,0,693,694,1,0,0,0,694,
        125,1,0,0,0,695,696,5,92,0,0,696,697,3,36,18,0,697,698,5,93,0,0,
        698,127,1,0,0,0,699,701,3,84,42,0,700,702,3,118,59,0,701,700,1,0,
        0,0,701,702,1,0,0,0,702,129,1,0,0,0,703,704,5,75,0,0,704,705,5,75,
        0,0,705,131,1,0,0,0,706,707,5,76,0,0,707,708,5,76,0,0,708,133,1,
        0,0,0,709,710,7,14,0,0,710,135,1,0,0,0,711,712,7,15,0,0,712,137,
        1,0,0,0,713,714,7,16,0,0,714,139,1,0,0,0,78,142,144,151,156,163,
        167,170,175,187,193,196,200,203,208,214,217,222,225,233,236,243,
        250,255,261,264,267,270,273,278,284,288,296,299,302,305,309,314,
        324,359,365,367,385,391,396,399,405,408,416,425,430,443,447,469,
        482,503,521,528,547,552,565,571,576,582,599,611,615,622,626,630,
        636,642,649,659,667,678,686,693,701
    ]

class EnforceParser ( Parser ):

    grammarFileName = "EnforceParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'enum'", "'switch'", "'extends'", 
                     "'const'", "'break'", "'case'", "'else'", "'for'", 
                     "'continue'", "'foreach'", "'if'", "'new'", "'return'", 
                     "'this'", "'thread'", "'void'", "'autoptr'", "'auto'", 
                     "'ref'", "'null'", "'notnull'", "'func'", "'native'", 
                     "'volatile'", "'proto'", "'static'", "'owned'", "'reference'", 
                     "'out'", "'protected'", "'event'", "'typedef'", "'modded'", 
                     "'override'", "'sealed'", "'inout'", "'super'", "'typename'", 
                     "'pointer'", "'goto'", "'private'", "'external'", "'delete'", 
                     "'local'", "'int'", "'float'", "'bool'", "'string'", 
                     "'vector'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'__LINE__'", "'__FILE__'", "'='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'++'", "'--'", "'+='", 
                     "'-='", "'*='", "'/='", "'|='", "'&='", "'<<='", "'>>='", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'|'", 
                     "'&'", "'~'", "'^'", "'&&'", "'||'", "'!'", "':'", 
                     "';'", "','", "'.'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "ENUM", "SWITCH", "EXTENDS", 
                      "CONST", "BREAK", "CASE", "ELSE", "FOR", "CONTINUE", 
                      "FOREACH", "IF", "NEW", "RETURN", "THIS", "THREAD", 
                      "VOID", "AUTOPTR", "AUTO", "REF", "NULL", "NOTNULL", 
                      "FUNC", "NATIVE", "VOLATILE", "PROTO", "STATIC", "OWNED", 
                      "REFERENCE", "OUT", "PROTECTED", "EVENT", "TYPEDEF", 
                      "MODDED", "OVERRIDE", "SEALED", "INOUT", "SUPER", 
                      "TYPENAME", "POINTER", "GOTO", "PRIVATE", "EXTERNAL", 
                      "DELETE", "LOCAL", "TYPE_INT", "TYPE_FLOAT", "TYPE_BOOL", 
                      "TYPE_STRING", "TYPE_VECTOR", "LiteralBoolean", "LiteralInteger", 
                      "LiteralFloat", "LiteralString", "PREPROC_LINE", "PREPROC_FILE", 
                      "Assign", "Add", "Subtract", "Multiply", "Divide", 
                      "Modulo", "Increment", "Decrement", "Add_Assign", 
                      "Subtract_Assign", "Multiply_Assign", "Divide_Assign", 
                      "Or_Assign", "And_Assign", "LShift_Assign", "RShift_Assign", 
                      "Equal", "Inequal", "Less", "Greater", "LessEqual", 
                      "GreaterEqual", "BitwiseOr", "BitwiseAnd", "BitwiseNot", 
                      "BitwiseXor", "LogicalAnd", "LogicalOr", "Bang", "Colon", 
                      "Semicolon", "Comma", "Dot", "LParenthesis", "RParenthesis", 
                      "LSBracket", "RSBracket", "LCurly", "RCurly", "WHITESPACES", 
                      "LineComment", "BlockComment", "IDENTIFIER", "WHILE", 
                      "DEFAULT" ]

    RULE_computationalStart = 0
    RULE_globalDeclaration = 1
    RULE_typeDeclaration = 2
    RULE_varAndFunctionBlock = 3
    RULE_variableDeclaration = 4
    RULE_variableDeclarators = 5
    RULE_variableDeclarator = 6
    RULE_functionDeclaration = 7
    RULE_functionParameters = 8
    RULE_functionParameter = 9
    RULE_classDeclaration = 10
    RULE_enumDeclaration = 11
    RULE_enumBody = 12
    RULE_enumValue = 13
    RULE_expression = 14
    RULE_castExpression = 15
    RULE_primaryExpression = 16
    RULE_objectCreation = 17
    RULE_functionCall = 18
    RULE_parenthesisedExpression = 19
    RULE_functionCallParameters = 20
    RULE_functionCallParameterList = 21
    RULE_functionCallParameter = 22
    RULE_optionalParameter = 23
    RULE_statementSingleOrBlock = 24
    RULE_statementBlock = 25
    RULE_statement = 26
    RULE_threadStatement = 27
    RULE_gotoStatement = 28
    RULE_ifStatement = 29
    RULE_elseStatement = 30
    RULE_deleteStatement = 31
    RULE_forStatement = 32
    RULE_foreachStatement = 33
    RULE_whileStatement = 34
    RULE_switchStatement = 35
    RULE_returnStatement = 36
    RULE_breakStatement = 37
    RULE_continueStatement = 38
    RULE_lambdaStatement = 39
    RULE_forControl = 40
    RULE_typeExtension_Child = 41
    RULE_identifier = 42
    RULE_expressionList = 43
    RULE_arrayIndex = 44
    RULE_literalArray = 45
    RULE_literalString = 46
    RULE_literalInteger = 47
    RULE_literalNull = 48
    RULE_literalFloat = 49
    RULE_literalBoolean = 50
    RULE_foreachVariable = 51
    RULE_switchLabel = 52
    RULE_defaultSwitchLabel = 53
    RULE_switchBlockStatementGroup = 54
    RULE_emptyBlock = 55
    RULE_typedefDeclaration = 56
    RULE_typedefType = 57
    RULE_keyword = 58
    RULE_typeList = 59
    RULE_genericType = 60
    RULE_genericTypeDeclarationList = 61
    RULE_genericTypeDeclaration = 62
    RULE_annotation = 63
    RULE_classReference = 64
    RULE_leftShift = 65
    RULE_rightShift = 66
    RULE_typeModifer = 67
    RULE_variableModifier = 68
    RULE_functionModifier = 69

    ruleNames =  [ "computationalStart", "globalDeclaration", "typeDeclaration", 
                   "varAndFunctionBlock", "variableDeclaration", "variableDeclarators", 
                   "variableDeclarator", "functionDeclaration", "functionParameters", 
                   "functionParameter", "classDeclaration", "enumDeclaration", 
                   "enumBody", "enumValue", "expression", "castExpression", 
                   "primaryExpression", "objectCreation", "functionCall", 
                   "parenthesisedExpression", "functionCallParameters", 
                   "functionCallParameterList", "functionCallParameter", 
                   "optionalParameter", "statementSingleOrBlock", "statementBlock", 
                   "statement", "threadStatement", "gotoStatement", "ifStatement", 
                   "elseStatement", "deleteStatement", "forStatement", "foreachStatement", 
                   "whileStatement", "switchStatement", "returnStatement", 
                   "breakStatement", "continueStatement", "lambdaStatement", 
                   "forControl", "typeExtension_Child", "identifier", "expressionList", 
                   "arrayIndex", "literalArray", "literalString", "literalInteger", 
                   "literalNull", "literalFloat", "literalBoolean", "foreachVariable", 
                   "switchLabel", "defaultSwitchLabel", "switchBlockStatementGroup", 
                   "emptyBlock", "typedefDeclaration", "typedefType", "keyword", 
                   "typeList", "genericType", "genericTypeDeclarationList", 
                   "genericTypeDeclaration", "annotation", "classReference", 
                   "leftShift", "rightShift", "typeModifer", "variableModifier", 
                   "functionModifier" ]

    EOF = Token.EOF
    CLASS=1
    ENUM=2
    SWITCH=3
    EXTENDS=4
    CONST=5
    BREAK=6
    CASE=7
    ELSE=8
    FOR=9
    CONTINUE=10
    FOREACH=11
    IF=12
    NEW=13
    RETURN=14
    THIS=15
    THREAD=16
    VOID=17
    AUTOPTR=18
    AUTO=19
    REF=20
    NULL=21
    NOTNULL=22
    FUNC=23
    NATIVE=24
    VOLATILE=25
    PROTO=26
    STATIC=27
    OWNED=28
    REFERENCE=29
    OUT=30
    PROTECTED=31
    EVENT=32
    TYPEDEF=33
    MODDED=34
    OVERRIDE=35
    SEALED=36
    INOUT=37
    SUPER=38
    TYPENAME=39
    POINTER=40
    GOTO=41
    PRIVATE=42
    EXTERNAL=43
    DELETE=44
    LOCAL=45
    TYPE_INT=46
    TYPE_FLOAT=47
    TYPE_BOOL=48
    TYPE_STRING=49
    TYPE_VECTOR=50
    LiteralBoolean=51
    LiteralInteger=52
    LiteralFloat=53
    LiteralString=54
    PREPROC_LINE=55
    PREPROC_FILE=56
    Assign=57
    Add=58
    Subtract=59
    Multiply=60
    Divide=61
    Modulo=62
    Increment=63
    Decrement=64
    Add_Assign=65
    Subtract_Assign=66
    Multiply_Assign=67
    Divide_Assign=68
    Or_Assign=69
    And_Assign=70
    LShift_Assign=71
    RShift_Assign=72
    Equal=73
    Inequal=74
    Less=75
    Greater=76
    LessEqual=77
    GreaterEqual=78
    BitwiseOr=79
    BitwiseAnd=80
    BitwiseNot=81
    BitwiseXor=82
    LogicalAnd=83
    LogicalOr=84
    Bang=85
    Colon=86
    Semicolon=87
    Comma=88
    Dot=89
    LParenthesis=90
    RParenthesis=91
    LSBracket=92
    RSBracket=93
    LCurly=94
    RCurly=95
    WHITESPACES=96
    LineComment=97
    BlockComment=98
    IDENTIFIER=99
    WHILE=100
    DEFAULT=101

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ComputationalStartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(EnforceParser.EOF, 0)

        def globalDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.GlobalDeclarationContext)
            else:
                return self.getTypedRuleContext(EnforceParser.GlobalDeclarationContext,i)


        def typeDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.TypeDeclarationContext)
            else:
                return self.getTypedRuleContext(EnforceParser.TypeDeclarationContext,i)


        def getRuleIndex(self):
            return EnforceParser.RULE_computationalStart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComputationalStart" ):
                listener.enterComputationalStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComputationalStart" ):
                listener.exitComputationalStart(self)




    def computationalStart(self):

        localctx = EnforceParser.ComputationalStartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_computationalStart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2230634212622374) != 0) or _la==92 or _la==99:
                self.state = 142
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 140
                    self.globalDeclaration()
                    pass

                elif la_ == 2:
                    self.state = 141
                    self.typeDeclaration()
                    pass


                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 147
            self.match(EnforceParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(EnforceParser.VariableDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(EnforceParser.FunctionDeclarationContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_globalDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalDeclaration" ):
                listener.enterGlobalDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalDeclaration" ):
                listener.exitGlobalDeclaration(self)




    def globalDeclaration(self):

        localctx = EnforceParser.GlobalDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_globalDeclaration)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.functionDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDeclaration(self):
            return self.getTypedRuleContext(EnforceParser.ClassDeclarationContext,0)


        def enumDeclaration(self):
            return self.getTypedRuleContext(EnforceParser.EnumDeclarationContext,0)


        def typedefDeclaration(self):
            return self.getTypedRuleContext(EnforceParser.TypedefDeclarationContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_typeDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDeclaration" ):
                listener.enterTypeDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDeclaration" ):
                listener.exitTypeDeclaration(self)




    def typeDeclaration(self):

        localctx = EnforceParser.TypeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_typeDeclaration)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.classDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.enumDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.typedefDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarAndFunctionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def globalDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.GlobalDeclarationContext)
            else:
                return self.getTypedRuleContext(EnforceParser.GlobalDeclarationContext,i)


        def LCurly(self):
            return self.getToken(EnforceParser.LCurly, 0)

        def RCurly(self):
            return self.getToken(EnforceParser.RCurly, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_varAndFunctionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarAndFunctionBlock" ):
                listener.enterVarAndFunctionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarAndFunctionBlock" ):
                listener.exitVarAndFunctionBlock(self)




    def varAndFunctionBlock(self):

        localctx = EnforceParser.VarAndFunctionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varAndFunctionBlock)
        self._la = 0 # Token type
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 35, 37, 39, 42, 43, 45, 46, 47, 48, 49, 50, 92, 99]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.globalDeclaration()
                pass
            elif token in [94]:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(EnforceParser.LCurly)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2230539723341856) != 0) or _la==92 or _la==99:
                    self.state = 160
                    self.globalDeclaration()
                    self.state = 165
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 166
                self.match(EnforceParser.RCurly)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.variableType = None # ClassReferenceContext

        def variableDeclarators(self):
            return self.getTypedRuleContext(EnforceParser.VariableDeclaratorsContext,0)


        def Semicolon(self):
            return self.getToken(EnforceParser.Semicolon, 0)

        def classReference(self):
            return self.getTypedRuleContext(EnforceParser.ClassReferenceContext,0)


        def annotation(self):
            return self.getTypedRuleContext(EnforceParser.AnnotationContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(EnforceParser.VariableModifierContext,i)


        def getRuleIndex(self):
            return EnforceParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = EnforceParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==92:
                self.state = 169
                self.annotation()


            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39724090916896) != 0):
                self.state = 172
                self.variableModifier()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            localctx.variableType = self.classReference()
            self.state = 179
            self.variableDeclarators()
            self.state = 180
            self.match(EnforceParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.VariableDeclaratorContext)
            else:
                return self.getTypedRuleContext(EnforceParser.VariableDeclaratorContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(EnforceParser.Comma)
            else:
                return self.getToken(EnforceParser.Comma, i)

        def getRuleIndex(self):
            return EnforceParser.RULE_variableDeclarators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarators" ):
                listener.enterVariableDeclarators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarators" ):
                listener.exitVariableDeclarators(self)




    def variableDeclarators(self):

        localctx = EnforceParser.VariableDeclaratorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variableDeclarators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.variableDeclarator()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==88:
                self.state = 183
                self.match(EnforceParser.Comma)
                self.state = 184
                self.variableDeclarator()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.variableName = None # IdentifierContext
            self.arrayLength = None # ExpressionContext
            self.variableValue = None # ExpressionContext

        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def LSBracket(self):
            return self.getToken(EnforceParser.LSBracket, 0)

        def RSBracket(self):
            return self.getToken(EnforceParser.RSBracket, 0)

        def Assign(self):
            return self.getToken(EnforceParser.Assign, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EnforceParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EnforceParser.RULE_variableDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarator" ):
                listener.enterVariableDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarator" ):
                listener.exitVariableDeclarator(self)




    def variableDeclarator(self):

        localctx = EnforceParser.VariableDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            localctx.variableName = self.identifier()
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==92:
                self.state = 191
                self.match(EnforceParser.LSBracket)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -8214635264423059456) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 35502817281) != 0):
                    self.state = 192
                    localctx.arrayLength = self.expression(0)


                self.state = 195
                self.match(EnforceParser.RSBracket)


            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 198
                self.match(EnforceParser.Assign)
                self.state = 199
                localctx.variableValue = self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.returnType = None # ClassReferenceContext
            self.deconstructor = None # Token
            self.functionName = None # IdentifierContext

        def functionParameters(self):
            return self.getTypedRuleContext(EnforceParser.FunctionParametersContext,0)


        def classReference(self):
            return self.getTypedRuleContext(EnforceParser.ClassReferenceContext,0)


        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def annotation(self):
            return self.getTypedRuleContext(EnforceParser.AnnotationContext,0)


        def functionModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.FunctionModifierContext)
            else:
                return self.getTypedRuleContext(EnforceParser.FunctionModifierContext,i)


        def LSBracket(self):
            return self.getToken(EnforceParser.LSBracket, 0)

        def RSBracket(self):
            return self.getToken(EnforceParser.RSBracket, 0)

        def statementSingleOrBlock(self):
            return self.getTypedRuleContext(EnforceParser.StatementSingleOrBlockContext,0)


        def Semicolon(self):
            return self.getToken(EnforceParser.Semicolon, 0)

        def BitwiseNot(self):
            return self.getToken(EnforceParser.BitwiseNot, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = EnforceParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==92:
                self.state = 202
                self.annotation()


            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13235999735808) != 0):
                self.state = 205
                self.functionModifier()
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 211
            localctx.returnType = self.classReference()
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==92:
                self.state = 212
                self.match(EnforceParser.LSBracket)
                self.state = 213
                self.match(EnforceParser.RSBracket)


            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==81:
                self.state = 216
                localctx.deconstructor = self.match(EnforceParser.BitwiseNot)


            self.state = 219
            localctx.functionName = self.identifier()
            self.state = 220
            self.functionParameters()
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 221
                self.statementSingleOrBlock()


            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 224
                self.match(EnforceParser.Semicolon)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LParenthesis(self):
            return self.getToken(EnforceParser.LParenthesis, 0)

        def RParenthesis(self):
            return self.getToken(EnforceParser.RParenthesis, 0)

        def functionParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.FunctionParameterContext)
            else:
                return self.getTypedRuleContext(EnforceParser.FunctionParameterContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(EnforceParser.Comma)
            else:
                return self.getToken(EnforceParser.Comma, i)

        def getRuleIndex(self):
            return EnforceParser.RULE_functionParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParameters" ):
                listener.enterFunctionParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParameters" ):
                listener.exitFunctionParameters(self)




    def functionParameters(self):

        localctx = EnforceParser.FunctionParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionParameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(EnforceParser.LParenthesis)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2221704925282336) != 0) or _la==99:
                self.state = 228
                self.functionParameter()
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==88:
                    self.state = 229
                    self.match(EnforceParser.Comma)
                    self.state = 230
                    self.functionParameter()
                    self.state = 235
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 238
            self.match(EnforceParser.RParenthesis)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.parameterType = None # ClassReferenceContext

        def variableDeclarator(self):
            return self.getTypedRuleContext(EnforceParser.VariableDeclaratorContext,0)


        def classReference(self):
            return self.getTypedRuleContext(EnforceParser.ClassReferenceContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(EnforceParser.VariableModifierContext,i)


        def getRuleIndex(self):
            return EnforceParser.RULE_functionParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParameter" ):
                listener.enterFunctionParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParameter" ):
                listener.exitFunctionParameter(self)




    def functionParameter(self):

        localctx = EnforceParser.FunctionParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39724090916896) != 0):
                self.state = 240
                self.variableModifier()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
            localctx.parameterType = self.classReference()
            self.state = 247
            self.variableDeclarator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.classname = None # IdentifierContext
            self.superclass = None # TypeExtension_ChildContext
            self.classBody = None # VarAndFunctionBlockContext

        def CLASS(self):
            return self.getToken(EnforceParser.CLASS, 0)

        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def annotation(self):
            return self.getTypedRuleContext(EnforceParser.AnnotationContext,0)


        def typeModifer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.TypeModiferContext)
            else:
                return self.getTypedRuleContext(EnforceParser.TypeModiferContext,i)


        def genericTypeDeclarationList(self):
            return self.getTypedRuleContext(EnforceParser.GenericTypeDeclarationListContext,0)


        def Semicolon(self):
            return self.getToken(EnforceParser.Semicolon, 0)

        def typeExtension_Child(self):
            return self.getTypedRuleContext(EnforceParser.TypeExtension_ChildContext,0)


        def varAndFunctionBlock(self):
            return self.getTypedRuleContext(EnforceParser.VarAndFunctionBlockContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)




    def classDeclaration(self):

        localctx = EnforceParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==92:
                self.state = 249
                self.annotation()


            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34 or _la==36:
                self.state = 252
                self.typeModifer()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 258
            self.match(EnforceParser.CLASS)
            self.state = 259
            localctx.classname = self.identifier()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==75:
                self.state = 260
                self.genericTypeDeclarationList()


            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4 or _la==86:
                self.state = 263
                localctx.superclass = self.typeExtension_Child()


            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 266
                localctx.classBody = self.varAndFunctionBlock()


            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==87:
                self.state = 269
                self.match(EnforceParser.Semicolon)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enumname = None # IdentifierContext
            self.superenum = None # TypeExtension_ChildContext

        def ENUM(self):
            return self.getToken(EnforceParser.ENUM, 0)

        def enumBody(self):
            return self.getTypedRuleContext(EnforceParser.EnumBodyContext,0)


        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def annotation(self):
            return self.getTypedRuleContext(EnforceParser.AnnotationContext,0)


        def typeModifer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.TypeModiferContext)
            else:
                return self.getTypedRuleContext(EnforceParser.TypeModiferContext,i)


        def Semicolon(self):
            return self.getToken(EnforceParser.Semicolon, 0)

        def typeExtension_Child(self):
            return self.getTypedRuleContext(EnforceParser.TypeExtension_ChildContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_enumDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumDeclaration" ):
                listener.enterEnumDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumDeclaration" ):
                listener.exitEnumDeclaration(self)




    def enumDeclaration(self):

        localctx = EnforceParser.EnumDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==92:
                self.state = 272
                self.annotation()


            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34 or _la==36:
                self.state = 275
                self.typeModifer()
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 281
            self.match(EnforceParser.ENUM)
            self.state = 282
            localctx.enumname = self.identifier()
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4 or _la==86:
                self.state = 283
                localctx.superenum = self.typeExtension_Child()


            self.state = 286
            self.enumBody()
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==87:
                self.state = 287
                self.match(EnforceParser.Semicolon)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCurly(self):
            return self.getToken(EnforceParser.LCurly, 0)

        def RCurly(self):
            return self.getToken(EnforceParser.RCurly, 0)

        def enumValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.EnumValueContext)
            else:
                return self.getTypedRuleContext(EnforceParser.EnumValueContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(EnforceParser.Comma)
            else:
                return self.getToken(EnforceParser.Comma, i)

        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(EnforceParser.Semicolon)
            else:
                return self.getToken(EnforceParser.Semicolon, i)

        def WHITESPACES(self, i:int=None):
            if i is None:
                return self.getTokens(EnforceParser.WHITESPACES)
            else:
                return self.getToken(EnforceParser.WHITESPACES, i)

        def getRuleIndex(self):
            return EnforceParser.RULE_enumBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumBody" ):
                listener.enterEnumBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumBody" ):
                listener.exitEnumBody(self)




    def enumBody(self):

        localctx = EnforceParser.EnumBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_enumBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(EnforceParser.LCurly)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2181980834365440) != 0) or _la==99:
                self.state = 291
                self.enumValue()
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 292
                        _la = self._input.LA(1)
                        if not(((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & 515) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 293
                        self.enumValue() 
                    self.state = 298
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)



            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==88:
                self.state = 301
                self.match(EnforceParser.Comma)


            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==87:
                self.state = 304
                self.match(EnforceParser.Semicolon)


            self.state = 307
            self.match(EnforceParser.RCurly)
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 308
                self.match(EnforceParser.Semicolon)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.itemname = None # IdentifierContext
            self.itemValue = None # ExpressionContext

        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def Assign(self):
            return self.getToken(EnforceParser.Assign, 0)

        def expression(self):
            return self.getTypedRuleContext(EnforceParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_enumValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumValue" ):
                listener.enterEnumValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumValue" ):
                listener.exitEnumValue(self)




    def enumValue(self):

        localctx = EnforceParser.EnumValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_enumValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            localctx.itemname = self.identifier()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 312
                self.match(EnforceParser.Assign)
                self.state = 313
                localctx.itemValue = self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.prefix = None # Token
            self.op = None # Token
            self.esVariable = None # IdentifierContext
            self.esFunction = None # FunctionCallContext
            self.suffix = None # Token

        def primaryExpression(self):
            return self.getTypedRuleContext(EnforceParser.PrimaryExpressionContext,0)


        def THIS(self):
            return self.getToken(EnforceParser.THIS, 0)

        def SUPER(self):
            return self.getToken(EnforceParser.SUPER, 0)

        def objectCreation(self):
            return self.getTypedRuleContext(EnforceParser.ObjectCreationContext,0)


        def castExpression(self):
            return self.getTypedRuleContext(EnforceParser.CastExpressionContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EnforceParser.ExpressionContext,i)


        def Increment(self):
            return self.getToken(EnforceParser.Increment, 0)

        def Decrement(self):
            return self.getToken(EnforceParser.Decrement, 0)

        def Bang(self):
            return self.getToken(EnforceParser.Bang, 0)

        def BitwiseNot(self):
            return self.getToken(EnforceParser.BitwiseNot, 0)

        def Add(self):
            return self.getToken(EnforceParser.Add, 0)

        def Subtract(self):
            return self.getToken(EnforceParser.Subtract, 0)

        def Multiply(self):
            return self.getToken(EnforceParser.Multiply, 0)

        def Divide(self):
            return self.getToken(EnforceParser.Divide, 0)

        def Modulo(self):
            return self.getToken(EnforceParser.Modulo, 0)

        def rightShift(self):
            return self.getTypedRuleContext(EnforceParser.RightShiftContext,0)


        def leftShift(self):
            return self.getTypedRuleContext(EnforceParser.LeftShiftContext,0)


        def LessEqual(self):
            return self.getToken(EnforceParser.LessEqual, 0)

        def GreaterEqual(self):
            return self.getToken(EnforceParser.GreaterEqual, 0)

        def Less(self):
            return self.getToken(EnforceParser.Less, 0)

        def Greater(self):
            return self.getToken(EnforceParser.Greater, 0)

        def Equal(self):
            return self.getToken(EnforceParser.Equal, 0)

        def Inequal(self):
            return self.getToken(EnforceParser.Inequal, 0)

        def BitwiseOr(self):
            return self.getToken(EnforceParser.BitwiseOr, 0)

        def BitwiseAnd(self):
            return self.getToken(EnforceParser.BitwiseAnd, 0)

        def BitwiseXor(self):
            return self.getToken(EnforceParser.BitwiseXor, 0)

        def LogicalAnd(self):
            return self.getToken(EnforceParser.LogicalAnd, 0)

        def LogicalOr(self):
            return self.getToken(EnforceParser.LogicalOr, 0)

        def Assign(self):
            return self.getToken(EnforceParser.Assign, 0)

        def Add_Assign(self):
            return self.getToken(EnforceParser.Add_Assign, 0)

        def Subtract_Assign(self):
            return self.getToken(EnforceParser.Subtract_Assign, 0)

        def Multiply_Assign(self):
            return self.getToken(EnforceParser.Multiply_Assign, 0)

        def Divide_Assign(self):
            return self.getToken(EnforceParser.Divide_Assign, 0)

        def Or_Assign(self):
            return self.getToken(EnforceParser.Or_Assign, 0)

        def And_Assign(self):
            return self.getToken(EnforceParser.And_Assign, 0)

        def LShift_Assign(self):
            return self.getToken(EnforceParser.LShift_Assign, 0)

        def RShift_Assign(self):
            return self.getToken(EnforceParser.RShift_Assign, 0)

        def Dot(self):
            return self.getToken(EnforceParser.Dot, 0)

        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(EnforceParser.FunctionCallContext,0)


        def arrayIndex(self):
            return self.getTypedRuleContext(EnforceParser.ArrayIndexContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EnforceParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 317
                self.primaryExpression()
                pass

            elif la_ == 2:
                self.state = 318
                self.match(EnforceParser.THIS)
                pass

            elif la_ == 3:
                self.state = 319
                self.match(EnforceParser.SUPER)
                pass

            elif la_ == 4:
                self.state = 320
                self.objectCreation()
                pass

            elif la_ == 5:
                self.state = 321
                self.castExpression()
                pass

            elif la_ == 6:
                self.state = 322
                localctx.prefix = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 58)) & ~0x3f) == 0 and ((1 << (_la - 58)) & 142606435) != 0)):
                    localctx.prefix = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 323
                self.expression(10)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 367
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 365
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        localctx = EnforceParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 326
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 327
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8070450532247928832) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 328
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = EnforceParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 329
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 330
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==58 or _la==59):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 331
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = EnforceParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 332
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 333
                        self.rightShift()
                        self.state = 334
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = EnforceParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 336
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 337
                        self.leftShift()
                        self.state = 338
                        self.expression(7)
                        pass

                    elif la_ == 5:
                        localctx = EnforceParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 340
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 341
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & 15) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 342
                        self.expression(6)
                        pass

                    elif la_ == 6:
                        localctx = EnforceParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 343
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 344
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==73 or _la==74):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 345
                        self.expression(5)
                        pass

                    elif la_ == 7:
                        localctx = EnforceParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 346
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 347
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((((_la - 79)) & ~0x3f) == 0 and ((1 << (_la - 79)) & 15) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 348
                        self.expression(4)
                        pass

                    elif la_ == 8:
                        localctx = EnforceParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 349
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 350
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==83 or _la==84):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 351
                        self.expression(3)
                        pass

                    elif la_ == 9:
                        localctx = EnforceParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 352
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 353
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((((_la - 57)) & ~0x3f) == 0 and ((1 << (_la - 57)) & 65281) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 354
                        self.expression(1)
                        pass

                    elif la_ == 10:
                        localctx = EnforceParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 355
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 356
                        localctx.op = self.match(EnforceParser.Dot)
                        self.state = 359
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                        if la_ == 1:
                            self.state = 357
                            localctx.esVariable = self.identifier()
                            pass

                        elif la_ == 2:
                            self.state = 358
                            localctx.esFunction = self.functionCall()
                            pass


                        pass

                    elif la_ == 11:
                        localctx = EnforceParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 361
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 362
                        self.arrayIndex()
                        pass

                    elif la_ == 12:
                        localctx = EnforceParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 363
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 364
                        localctx.suffix = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==63 or _la==64):
                            localctx.suffix = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 369
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CastExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cast = None # ClassReferenceContext

        def LParenthesis(self):
            return self.getToken(EnforceParser.LParenthesis, 0)

        def RParenthesis(self):
            return self.getToken(EnforceParser.RParenthesis, 0)

        def expression(self):
            return self.getTypedRuleContext(EnforceParser.ExpressionContext,0)


        def classReference(self):
            return self.getTypedRuleContext(EnforceParser.ClassReferenceContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_castExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastExpression" ):
                listener.enterCastExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastExpression" ):
                listener.exitCastExpression(self)




    def castExpression(self):

        localctx = EnforceParser.CastExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_castExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(EnforceParser.LParenthesis)
            self.state = 371
            localctx.cast = self.classReference()
            self.state = 372
            self.match(EnforceParser.RParenthesis)
            self.state = 373
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.esFunction = None # FunctionCallContext
            self.esString = None # LiteralStringContext
            self.esInt = None # LiteralIntegerContext
            self.esFloat = None # LiteralFloatContext
            self.esBool = None # LiteralBooleanContext
            self.parExpression = None # ParenthesisedExpressionContext
            self.esArray = None # LiteralArrayContext
            self.esNull = None # LiteralNullContext
            self.esVariable = None # IdentifierContext
            self.esGeneric = None # ClassReferenceContext

        def functionCall(self):
            return self.getTypedRuleContext(EnforceParser.FunctionCallContext,0)


        def literalString(self):
            return self.getTypedRuleContext(EnforceParser.LiteralStringContext,0)


        def literalInteger(self):
            return self.getTypedRuleContext(EnforceParser.LiteralIntegerContext,0)


        def literalFloat(self):
            return self.getTypedRuleContext(EnforceParser.LiteralFloatContext,0)


        def literalBoolean(self):
            return self.getTypedRuleContext(EnforceParser.LiteralBooleanContext,0)


        def parenthesisedExpression(self):
            return self.getTypedRuleContext(EnforceParser.ParenthesisedExpressionContext,0)


        def literalArray(self):
            return self.getTypedRuleContext(EnforceParser.LiteralArrayContext,0)


        def literalNull(self):
            return self.getTypedRuleContext(EnforceParser.LiteralNullContext,0)


        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def classReference(self):
            return self.getTypedRuleContext(EnforceParser.ClassReferenceContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)




    def primaryExpression(self):

        localctx = EnforceParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_primaryExpression)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                localctx.esFunction = self.functionCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                localctx.esString = self.literalString()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                localctx.esInt = self.literalInteger()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 378
                localctx.esFloat = self.literalFloat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 379
                localctx.esBool = self.literalBoolean()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 380
                localctx.parExpression = self.parenthesisedExpression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 381
                localctx.esArray = self.literalArray()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 382
                localctx.esNull = self.literalNull()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 383
                localctx.esVariable = self.identifier()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 384
                localctx.esGeneric = self.classReference()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectCreationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.objectName = None # IdentifierContext

        def NEW(self):
            return self.getToken(EnforceParser.NEW, 0)

        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(EnforceParser.VariableModifierContext,i)


        def typeList(self):
            return self.getTypedRuleContext(EnforceParser.TypeListContext,0)


        def functionCallParameters(self):
            return self.getTypedRuleContext(EnforceParser.FunctionCallParametersContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_objectCreation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectCreation" ):
                listener.enterObjectCreation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectCreation" ):
                listener.exitObjectCreation(self)




    def objectCreation(self):

        localctx = EnforceParser.ObjectCreationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_objectCreation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(EnforceParser.NEW)
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39724090916896) != 0):
                self.state = 388
                self.variableModifier()
                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 394
            localctx.objectName = self.identifier()
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 395
                self.typeList()


            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 398
                self.functionCallParameters()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def functionCallParameters(self):
            return self.getTypedRuleContext(EnforceParser.FunctionCallParametersContext,0)


        def LSBracket(self):
            return self.getToken(EnforceParser.LSBracket, 0)

        def RSBracket(self):
            return self.getToken(EnforceParser.RSBracket, 0)

        def expression(self):
            return self.getTypedRuleContext(EnforceParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = EnforceParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.identifier()
            self.state = 402
            self.functionCallParameters()
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 403
                self.match(EnforceParser.LSBracket)
                self.state = 405
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -8214635264423059456) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 35502817281) != 0):
                    self.state = 404
                    self.expression(0)


                self.state = 407
                self.match(EnforceParser.RSBracket)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenthesisedExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LParenthesis(self):
            return self.getToken(EnforceParser.LParenthesis, 0)

        def expression(self):
            return self.getTypedRuleContext(EnforceParser.ExpressionContext,0)


        def RParenthesis(self):
            return self.getToken(EnforceParser.RParenthesis, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_parenthesisedExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesisedExpression" ):
                listener.enterParenthesisedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesisedExpression" ):
                listener.exitParenthesisedExpression(self)




    def parenthesisedExpression(self):

        localctx = EnforceParser.ParenthesisedExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parenthesisedExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(EnforceParser.LParenthesis)
            self.state = 411
            self.expression(0)
            self.state = 412
            self.match(EnforceParser.RParenthesis)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LParenthesis(self):
            return self.getToken(EnforceParser.LParenthesis, 0)

        def RParenthesis(self):
            return self.getToken(EnforceParser.RParenthesis, 0)

        def functionCallParameterList(self):
            return self.getTypedRuleContext(EnforceParser.FunctionCallParameterListContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_functionCallParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallParameters" ):
                listener.enterFunctionCallParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallParameters" ):
                listener.exitFunctionCallParameters(self)




    def functionCallParameters(self):

        localctx = EnforceParser.FunctionCallParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_functionCallParameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(EnforceParser.LParenthesis)
            self.state = 416
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -8214635264423059456) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 35502817281) != 0):
                self.state = 415
                self.functionCallParameterList()


            self.state = 418
            self.match(EnforceParser.RParenthesis)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCallParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.FunctionCallParameterContext)
            else:
                return self.getTypedRuleContext(EnforceParser.FunctionCallParameterContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(EnforceParser.Comma)
            else:
                return self.getToken(EnforceParser.Comma, i)

        def getRuleIndex(self):
            return EnforceParser.RULE_functionCallParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallParameterList" ):
                listener.enterFunctionCallParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallParameterList" ):
                listener.exitFunctionCallParameterList(self)




    def functionCallParameterList(self):

        localctx = EnforceParser.FunctionCallParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_functionCallParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.functionCallParameter()
            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==88:
                self.state = 421
                self.match(EnforceParser.Comma)
                self.state = 422
                self.functionCallParameter()
                self.state = 427
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(EnforceParser.ExpressionContext,0)


        def optionalParameter(self):
            return self.getTypedRuleContext(EnforceParser.OptionalParameterContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_functionCallParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallParameter" ):
                listener.enterFunctionCallParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallParameter" ):
                listener.exitFunctionCallParameter(self)




    def functionCallParameter(self):

        localctx = EnforceParser.FunctionCallParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_functionCallParameter)
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.optionalParameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionalParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.argumentName = None # IdentifierContext
            self.argumentValue = None # ExpressionContext

        def Colon(self):
            return self.getToken(EnforceParser.Colon, 0)

        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(EnforceParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_optionalParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionalParameter" ):
                listener.enterOptionalParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionalParameter" ):
                listener.exitOptionalParameter(self)




    def optionalParameter(self):

        localctx = EnforceParser.OptionalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_optionalParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            localctx.argumentName = self.identifier()
            self.state = 433
            self.match(EnforceParser.Colon)
            self.state = 434
            localctx.argumentValue = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementSingleOrBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(EnforceParser.StatementContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_statementSingleOrBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementSingleOrBlock" ):
                listener.enterStatementSingleOrBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementSingleOrBlock" ):
                listener.exitStatementSingleOrBlock(self)




    def statementSingleOrBlock(self):

        localctx = EnforceParser.StatementSingleOrBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_statementSingleOrBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def emptyBlock(self):
            return self.getTypedRuleContext(EnforceParser.EmptyBlockContext,0)


        def LCurly(self):
            return self.getToken(EnforceParser.LCurly, 0)

        def RCurly(self):
            return self.getToken(EnforceParser.RCurly, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.StatementContext)
            else:
                return self.getTypedRuleContext(EnforceParser.StatementContext,i)


        def getRuleIndex(self):
            return EnforceParser.RULE_statementBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementBlock" ):
                listener.enterStatementBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementBlock" ):
                listener.exitStatementBlock(self)




    def statementBlock(self):

        localctx = EnforceParser.StatementBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_statementBlock)
        self._la = 0 # Token type
        try:
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.emptyBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.match(EnforceParser.LCurly)
                self.state = 443
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & -8214575749122752920) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 104499118081) != 0):
                    self.state = 440
                    self.statement()
                    self.state = 445
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 446
                self.match(EnforceParser.RCurly)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.expressionaryStatement = None # ExpressionContext
            self.esVariableDeclaration = None # VariableDeclarationContext
            self.esDelete = None # DeleteStatementContext
            self.esIf = None # IfStatementContext
            self.esFor = None # ForStatementContext
            self.esForEach = None # ForeachStatementContext
            self.esWhile = None # WhileStatementContext
            self.esSwitch = None # SwitchStatementContext
            self.esReturn = None # ReturnStatementContext
            self.esBreak = None # BreakStatementContext
            self.esContinue = None # ContinueStatementContext
            self.esStatementBlock = None # StatementBlockContext
            self.esGoto = None # GotoStatementContext
            self.esLambda = None # LambdaStatementContext
            self.esThread = None # ThreadStatementContext
            self.esSemicolon = None # Token

        def Semicolon(self):
            return self.getToken(EnforceParser.Semicolon, 0)

        def expression(self):
            return self.getTypedRuleContext(EnforceParser.ExpressionContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(EnforceParser.VariableDeclarationContext,0)


        def deleteStatement(self):
            return self.getTypedRuleContext(EnforceParser.DeleteStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(EnforceParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(EnforceParser.ForStatementContext,0)


        def foreachStatement(self):
            return self.getTypedRuleContext(EnforceParser.ForeachStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(EnforceParser.WhileStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(EnforceParser.SwitchStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(EnforceParser.ReturnStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(EnforceParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(EnforceParser.ContinueStatementContext,0)


        def statementBlock(self):
            return self.getTypedRuleContext(EnforceParser.StatementBlockContext,0)


        def gotoStatement(self):
            return self.getTypedRuleContext(EnforceParser.GotoStatementContext,0)


        def lambdaStatement(self):
            return self.getTypedRuleContext(EnforceParser.LambdaStatementContext,0)


        def threadStatement(self):
            return self.getTypedRuleContext(EnforceParser.ThreadStatementContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = EnforceParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_statement)
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                localctx.expressionaryStatement = self.expression(0)
                self.state = 450
                self.match(EnforceParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                localctx.esVariableDeclaration = self.variableDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 453
                localctx.esDelete = self.deleteStatement()
                self.state = 454
                self.match(EnforceParser.Semicolon)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 456
                localctx.esIf = self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 457
                localctx.esFor = self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 458
                localctx.esForEach = self.foreachStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 459
                localctx.esWhile = self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 460
                localctx.esSwitch = self.switchStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 461
                localctx.esReturn = self.returnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 462
                localctx.esBreak = self.breakStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 463
                localctx.esContinue = self.continueStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 464
                localctx.esStatementBlock = self.statementBlock()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 465
                localctx.esGoto = self.gotoStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 466
                localctx.esLambda = self.lambdaStatement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 467
                localctx.esThread = self.threadStatement()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 468
                localctx.esSemicolon = self.match(EnforceParser.Semicolon)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThreadStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THREAD(self):
            return self.getToken(EnforceParser.THREAD, 0)

        def functionCall(self):
            return self.getTypedRuleContext(EnforceParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_threadStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThreadStatement" ):
                listener.enterThreadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThreadStatement" ):
                listener.exitThreadStatement(self)




    def threadStatement(self):

        localctx = EnforceParser.ThreadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_threadStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(EnforceParser.THREAD)
            self.state = 472
            self.functionCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOTO(self):
            return self.getToken(EnforceParser.GOTO, 0)

        def expression(self):
            return self.getTypedRuleContext(EnforceParser.ExpressionContext,0)


        def Semicolon(self):
            return self.getToken(EnforceParser.Semicolon, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_gotoStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotoStatement" ):
                listener.enterGotoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotoStatement" ):
                listener.exitGotoStatement(self)




    def gotoStatement(self):

        localctx = EnforceParser.GotoStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_gotoStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(EnforceParser.GOTO)
            self.state = 475
            self.expression(0)
            self.state = 476
            self.match(EnforceParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.condition = None # ParenthesisedExpressionContext
            self.ifBody = None # StatementSingleOrBlockContext

        def IF(self):
            return self.getToken(EnforceParser.IF, 0)

        def parenthesisedExpression(self):
            return self.getTypedRuleContext(EnforceParser.ParenthesisedExpressionContext,0)


        def statementSingleOrBlock(self):
            return self.getTypedRuleContext(EnforceParser.StatementSingleOrBlockContext,0)


        def elseStatement(self):
            return self.getTypedRuleContext(EnforceParser.ElseStatementContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = EnforceParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(EnforceParser.IF)
            self.state = 479
            localctx.condition = self.parenthesisedExpression()
            self.state = 480
            localctx.ifBody = self.statementSingleOrBlock()
            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 481
                self.elseStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.elseBody = None # StatementSingleOrBlockContext

        def ELSE(self):
            return self.getToken(EnforceParser.ELSE, 0)

        def statementSingleOrBlock(self):
            return self.getTypedRuleContext(EnforceParser.StatementSingleOrBlockContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_elseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStatement" ):
                listener.enterElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStatement" ):
                listener.exitElseStatement(self)




    def elseStatement(self):

        localctx = EnforceParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(EnforceParser.ELSE)
            self.state = 485
            localctx.elseBody = self.statementSingleOrBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(EnforceParser.DELETE, 0)

        def expression(self):
            return self.getTypedRuleContext(EnforceParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_deleteStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteStatement" ):
                listener.enterDeleteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteStatement" ):
                listener.exitDeleteStatement(self)




    def deleteStatement(self):

        localctx = EnforceParser.DeleteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_deleteStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(EnforceParser.DELETE)
            self.state = 488
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.loopBody = None # StatementSingleOrBlockContext

        def FOR(self):
            return self.getToken(EnforceParser.FOR, 0)

        def LParenthesis(self):
            return self.getToken(EnforceParser.LParenthesis, 0)

        def forControl(self):
            return self.getTypedRuleContext(EnforceParser.ForControlContext,0)


        def RParenthesis(self):
            return self.getToken(EnforceParser.RParenthesis, 0)

        def statementSingleOrBlock(self):
            return self.getTypedRuleContext(EnforceParser.StatementSingleOrBlockContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)




    def forStatement(self):

        localctx = EnforceParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(EnforceParser.FOR)
            self.state = 491
            self.match(EnforceParser.LParenthesis)
            self.state = 492
            self.forControl()
            self.state = 493
            self.match(EnforceParser.RParenthesis)
            self.state = 494
            localctx.loopBody = self.statementSingleOrBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForeachStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enumerating = None # ExpressionContext
            self.loopBody = None # StatementSingleOrBlockContext

        def FOREACH(self):
            return self.getToken(EnforceParser.FOREACH, 0)

        def LParenthesis(self):
            return self.getToken(EnforceParser.LParenthesis, 0)

        def foreachVariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.ForeachVariableContext)
            else:
                return self.getTypedRuleContext(EnforceParser.ForeachVariableContext,i)


        def Colon(self):
            return self.getToken(EnforceParser.Colon, 0)

        def RParenthesis(self):
            return self.getToken(EnforceParser.RParenthesis, 0)

        def expression(self):
            return self.getTypedRuleContext(EnforceParser.ExpressionContext,0)


        def statementSingleOrBlock(self):
            return self.getTypedRuleContext(EnforceParser.StatementSingleOrBlockContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(EnforceParser.Comma)
            else:
                return self.getToken(EnforceParser.Comma, i)

        def getRuleIndex(self):
            return EnforceParser.RULE_foreachStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForeachStatement" ):
                listener.enterForeachStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForeachStatement" ):
                listener.exitForeachStatement(self)




    def foreachStatement(self):

        localctx = EnforceParser.ForeachStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_foreachStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(EnforceParser.FOREACH)
            self.state = 497
            self.match(EnforceParser.LParenthesis)
            self.state = 498
            self.foreachVariable()
            self.state = 503
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==88:
                self.state = 499
                self.match(EnforceParser.Comma)
                self.state = 500
                self.foreachVariable()
                self.state = 505
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 506
            self.match(EnforceParser.Colon)
            self.state = 507
            localctx.enumerating = self.expression(0)
            self.state = 508
            self.match(EnforceParser.RParenthesis)
            self.state = 509
            localctx.loopBody = self.statementSingleOrBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.condition = None # ParenthesisedExpressionContext
            self.loopBody = None # StatementSingleOrBlockContext

        def WHILE(self):
            return self.getToken(EnforceParser.WHILE, 0)

        def parenthesisedExpression(self):
            return self.getTypedRuleContext(EnforceParser.ParenthesisedExpressionContext,0)


        def statementSingleOrBlock(self):
            return self.getTypedRuleContext(EnforceParser.StatementSingleOrBlockContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = EnforceParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(EnforceParser.WHILE)
            self.state = 512
            localctx.condition = self.parenthesisedExpression()
            self.state = 513
            localctx.loopBody = self.statementSingleOrBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(EnforceParser.SWITCH, 0)

        def parenthesisedExpression(self):
            return self.getTypedRuleContext(EnforceParser.ParenthesisedExpressionContext,0)


        def LCurly(self):
            return self.getToken(EnforceParser.LCurly, 0)

        def RCurly(self):
            return self.getToken(EnforceParser.RCurly, 0)

        def switchBlockStatementGroup(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.SwitchBlockStatementGroupContext)
            else:
                return self.getTypedRuleContext(EnforceParser.SwitchBlockStatementGroupContext,i)


        def getRuleIndex(self):
            return EnforceParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)




    def switchStatement(self):

        localctx = EnforceParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(EnforceParser.SWITCH)
            self.state = 516
            self.parenthesisedExpression()
            self.state = 517
            self.match(EnforceParser.LCurly)
            self.state = 521
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==101:
                self.state = 518
                self.switchBlockStatementGroup()
                self.state = 523
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 524
            self.match(EnforceParser.RCurly)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(EnforceParser.RETURN, 0)

        def Semicolon(self):
            return self.getToken(EnforceParser.Semicolon, 0)

        def expression(self):
            return self.getTypedRuleContext(EnforceParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = EnforceParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(EnforceParser.RETURN)
            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -8214635264423059456) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 35502817281) != 0):
                self.state = 527
                self.expression(0)


            self.state = 530
            self.match(EnforceParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(EnforceParser.BREAK, 0)

        def Semicolon(self):
            return self.getToken(EnforceParser.Semicolon, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)




    def breakStatement(self):

        localctx = EnforceParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(EnforceParser.BREAK)
            self.state = 533
            self.match(EnforceParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(EnforceParser.CONTINUE, 0)

        def Semicolon(self):
            return self.getToken(EnforceParser.Semicolon, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)




    def continueStatement(self):

        localctx = EnforceParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            self.match(EnforceParser.CONTINUE)
            self.state = 536
            self.match(EnforceParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.lambdaType = None # ClassReferenceContext
            self.lambdaName = None # IdentifierContext
            self.lambdaArguments = None # FunctionCallParametersContext

        def Semicolon(self):
            return self.getToken(EnforceParser.Semicolon, 0)

        def classReference(self):
            return self.getTypedRuleContext(EnforceParser.ClassReferenceContext,0)


        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def functionCallParameters(self):
            return self.getTypedRuleContext(EnforceParser.FunctionCallParametersContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_lambdaStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaStatement" ):
                listener.enterLambdaStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaStatement" ):
                listener.exitLambdaStatement(self)




    def lambdaStatement(self):

        localctx = EnforceParser.LambdaStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_lambdaStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            localctx.lambdaType = self.classReference()
            self.state = 539
            localctx.lambdaName = self.identifier()
            self.state = 540
            localctx.lambdaArguments = self.functionCallParameters()
            self.state = 541
            self.match(EnforceParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForControlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.forInit = None # StatementContext
            self.forCondition = None # ExpressionContext
            self.forIteration = None # ExpressionContext

        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(EnforceParser.Semicolon)
            else:
                return self.getToken(EnforceParser.Semicolon, i)

        def statement(self):
            return self.getTypedRuleContext(EnforceParser.StatementContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EnforceParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EnforceParser.RULE_forControl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForControl" ):
                listener.enterForControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForControl" ):
                listener.exitForControl(self)




    def forControl(self):

        localctx = EnforceParser.ForControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_forControl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            localctx.forInit = self.statement()
            self.state = 544
            localctx.forCondition = self.expression(0)
            self.state = 545
            self.match(EnforceParser.Semicolon)
            self.state = 547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -8214635264423059456) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 35502817281) != 0):
                self.state = 546
                localctx.forIteration = self.expression(0)


            self.state = 552
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==87:
                self.state = 549
                self.match(EnforceParser.Semicolon)
                self.state = 554
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeExtension_ChildContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.extends = None # Token
            self.classname = None # ClassReferenceContext

        def classReference(self):
            return self.getTypedRuleContext(EnforceParser.ClassReferenceContext,0)


        def EXTENDS(self):
            return self.getToken(EnforceParser.EXTENDS, 0)

        def Colon(self):
            return self.getToken(EnforceParser.Colon, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_typeExtension_Child

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeExtension_Child" ):
                listener.enterTypeExtension_Child(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeExtension_Child" ):
                listener.exitTypeExtension_Child(self)




    def typeExtension_Child(self):

        localctx = EnforceParser.TypeExtension_ChildContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_typeExtension_Child)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            localctx.extends = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==4 or _la==86):
                localctx.extends = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 556
            localctx.classname = self.classReference()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(EnforceParser.IDENTIFIER, 0)

        def TYPE_INT(self):
            return self.getToken(EnforceParser.TYPE_INT, 0)

        def TYPE_BOOL(self):
            return self.getToken(EnforceParser.TYPE_BOOL, 0)

        def TYPE_FLOAT(self):
            return self.getToken(EnforceParser.TYPE_FLOAT, 0)

        def TYPE_STRING(self):
            return self.getToken(EnforceParser.TYPE_STRING, 0)

        def TYPE_VECTOR(self):
            return self.getToken(EnforceParser.TYPE_VECTOR, 0)

        def VOID(self):
            return self.getToken(EnforceParser.VOID, 0)

        def AUTO(self):
            return self.getToken(EnforceParser.AUTO, 0)

        def TYPENAME(self):
            return self.getToken(EnforceParser.TYPENAME, 0)

        def FUNC(self):
            return self.getToken(EnforceParser.FUNC, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = EnforceParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2181980834365440) != 0) or _la==99):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EnforceParser.ExpressionContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(EnforceParser.Comma)
            else:
                return self.getToken(EnforceParser.Comma, i)

        def getRuleIndex(self):
            return EnforceParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = EnforceParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.expression(0)
            self.state = 565
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 561
                    self.match(EnforceParser.Comma)
                    self.state = 562
                    self.expression(0) 
                self.state = 567
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

            self.state = 571
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==88:
                self.state = 568
                self.match(EnforceParser.Comma)
                self.state = 573
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayIndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSBracket(self):
            return self.getToken(EnforceParser.LSBracket, 0)

        def RSBracket(self):
            return self.getToken(EnforceParser.RSBracket, 0)

        def expression(self):
            return self.getTypedRuleContext(EnforceParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_arrayIndex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayIndex" ):
                listener.enterArrayIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayIndex" ):
                listener.exitArrayIndex(self)




    def arrayIndex(self):

        localctx = EnforceParser.ArrayIndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_arrayIndex)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(EnforceParser.LSBracket)
            self.state = 576
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -8214635264423059456) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 35502817281) != 0):
                self.state = 575
                self.expression(0)


            self.state = 578
            self.match(EnforceParser.RSBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCurly(self):
            return self.getToken(EnforceParser.LCurly, 0)

        def RCurly(self):
            return self.getToken(EnforceParser.RCurly, 0)

        def expressionList(self):
            return self.getTypedRuleContext(EnforceParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_literalArray

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralArray" ):
                listener.enterLiteralArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralArray" ):
                listener.exitLiteralArray(self)




    def literalArray(self):

        localctx = EnforceParser.LiteralArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_literalArray)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.match(EnforceParser.LCurly)
            self.state = 582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -8214635264423059456) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 35502817281) != 0):
                self.state = 581
                self.expressionList()


            self.state = 584
            self.match(EnforceParser.RCurly)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LiteralString(self):
            return self.getToken(EnforceParser.LiteralString, 0)

        def PREPROC_LINE(self):
            return self.getToken(EnforceParser.PREPROC_LINE, 0)

        def PREPROC_FILE(self):
            return self.getToken(EnforceParser.PREPROC_FILE, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_literalString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralString" ):
                listener.enterLiteralString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralString" ):
                listener.exitLiteralString(self)




    def literalString(self):

        localctx = EnforceParser.LiteralStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_literalString)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126100789566373888) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralIntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LiteralInteger(self):
            return self.getToken(EnforceParser.LiteralInteger, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_literalInteger

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralInteger" ):
                listener.enterLiteralInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralInteger" ):
                listener.exitLiteralInteger(self)




    def literalInteger(self):

        localctx = EnforceParser.LiteralIntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_literalInteger)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.match(EnforceParser.LiteralInteger)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralNullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL(self):
            return self.getToken(EnforceParser.NULL, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_literalNull

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralNull" ):
                listener.enterLiteralNull(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralNull" ):
                listener.exitLiteralNull(self)




    def literalNull(self):

        localctx = EnforceParser.LiteralNullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_literalNull)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            self.match(EnforceParser.NULL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralFloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LiteralFloat(self):
            return self.getToken(EnforceParser.LiteralFloat, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_literalFloat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralFloat" ):
                listener.enterLiteralFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralFloat" ):
                listener.exitLiteralFloat(self)




    def literalFloat(self):

        localctx = EnforceParser.LiteralFloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_literalFloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(EnforceParser.LiteralFloat)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralBooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LiteralBoolean(self):
            return self.getToken(EnforceParser.LiteralBoolean, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_literalBoolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralBoolean" ):
                listener.enterLiteralBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralBoolean" ):
                listener.exitLiteralBoolean(self)




    def literalBoolean(self):

        localctx = EnforceParser.LiteralBooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_literalBoolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(EnforceParser.LiteralBoolean)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForeachVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.iteratedVariableType = None # ClassReferenceContext
            self.iteratedVariableName = None # IdentifierContext

        def classReference(self):
            return self.getTypedRuleContext(EnforceParser.ClassReferenceContext,0)


        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(EnforceParser.VariableModifierContext,i)


        def getRuleIndex(self):
            return EnforceParser.RULE_foreachVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForeachVariable" ):
                listener.enterForeachVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForeachVariable" ):
                listener.exitForeachVariable(self)




    def foreachVariable(self):

        localctx = EnforceParser.ForeachVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_foreachVariable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39724090916896) != 0):
                self.state = 596
                self.variableModifier()
                self.state = 601
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 602
            localctx.iteratedVariableType = self.classReference()
            self.state = 603
            localctx.iteratedVariableName = self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(EnforceParser.CASE, 0)

        def Colon(self):
            return self.getToken(EnforceParser.Colon, 0)

        def expression(self):
            return self.getTypedRuleContext(EnforceParser.ExpressionContext,0)


        def statementSingleOrBlock(self):
            return self.getTypedRuleContext(EnforceParser.StatementSingleOrBlockContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.StatementContext)
            else:
                return self.getTypedRuleContext(EnforceParser.StatementContext,i)


        def getRuleIndex(self):
            return EnforceParser.RULE_switchLabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchLabel" ):
                listener.enterSwitchLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchLabel" ):
                listener.exitSwitchLabel(self)




    def switchLabel(self):

        localctx = EnforceParser.SwitchLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_switchLabel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.match(EnforceParser.CASE)

            self.state = 606
            self.expression(0)
            self.state = 607
            self.match(EnforceParser.Colon)
            self.state = 615
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 611
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & -8214575749122752920) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 104499118081) != 0):
                    self.state = 608
                    self.statement()
                    self.state = 613
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 614
                self.statementSingleOrBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultSwitchLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(EnforceParser.DEFAULT, 0)

        def Colon(self):
            return self.getToken(EnforceParser.Colon, 0)

        def statementSingleOrBlock(self):
            return self.getTypedRuleContext(EnforceParser.StatementSingleOrBlockContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.StatementContext)
            else:
                return self.getTypedRuleContext(EnforceParser.StatementContext,i)


        def getRuleIndex(self):
            return EnforceParser.RULE_defaultSwitchLabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultSwitchLabel" ):
                listener.enterDefaultSwitchLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultSwitchLabel" ):
                listener.exitDefaultSwitchLabel(self)




    def defaultSwitchLabel(self):

        localctx = EnforceParser.DefaultSwitchLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_defaultSwitchLabel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self.match(EnforceParser.DEFAULT)
            self.state = 618
            self.match(EnforceParser.Colon)
            self.state = 626
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 622
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & -8214575749122752920) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 104499118081) != 0):
                    self.state = 619
                    self.statement()
                    self.state = 624
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 625
                self.statementSingleOrBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchBlockStatementGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switchLabel(self):
            return self.getTypedRuleContext(EnforceParser.SwitchLabelContext,0)


        def defaultSwitchLabel(self):
            return self.getTypedRuleContext(EnforceParser.DefaultSwitchLabelContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_switchBlockStatementGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchBlockStatementGroup" ):
                listener.enterSwitchBlockStatementGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchBlockStatementGroup" ):
                listener.exitSwitchBlockStatementGroup(self)




    def switchBlockStatementGroup(self):

        localctx = EnforceParser.SwitchBlockStatementGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_switchBlockStatementGroup)
        try:
            self.state = 630
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 628
                self.switchLabel()
                pass
            elif token in [101]:
                self.enterOuterAlt(localctx, 2)
                self.state = 629
                self.defaultSwitchLabel()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCurly(self):
            return self.getToken(EnforceParser.LCurly, 0)

        def RCurly(self):
            return self.getToken(EnforceParser.RCurly, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_emptyBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyBlock" ):
                listener.enterEmptyBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyBlock" ):
                listener.exitEmptyBlock(self)




    def emptyBlock(self):

        localctx = EnforceParser.EmptyBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_emptyBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.match(EnforceParser.LCurly)
            self.state = 633
            self.match(EnforceParser.RCurly)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedefDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.fromType = None # TypedefTypeContext
            self.toType = None # IdentifierContext

        def TYPEDEF(self):
            return self.getToken(EnforceParser.TYPEDEF, 0)

        def Semicolon(self):
            return self.getToken(EnforceParser.Semicolon, 0)

        def typedefType(self):
            return self.getTypedRuleContext(EnforceParser.TypedefTypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def annotation(self):
            return self.getTypedRuleContext(EnforceParser.AnnotationContext,0)


        def LSBracket(self):
            return self.getToken(EnforceParser.LSBracket, 0)

        def RSBracket(self):
            return self.getToken(EnforceParser.RSBracket, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_typedefDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedefDeclaration" ):
                listener.enterTypedefDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedefDeclaration" ):
                listener.exitTypedefDeclaration(self)




    def typedefDeclaration(self):

        localctx = EnforceParser.TypedefDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_typedefDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 636
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==92:
                self.state = 635
                self.annotation()


            self.state = 638
            self.match(EnforceParser.TYPEDEF)
            self.state = 639
            localctx.fromType = self.typedefType()
            self.state = 642
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==92:
                self.state = 640
                self.match(EnforceParser.LSBracket)
                self.state = 641
                self.match(EnforceParser.RSBracket)


            self.state = 644
            localctx.toType = self.identifier()
            self.state = 645
            self.match(EnforceParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedefTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(EnforceParser.KeywordContext,0)


        def classReference(self):
            return self.getTypedRuleContext(EnforceParser.ClassReferenceContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_typedefType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedefType" ):
                listener.enterTypedefType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedefType" ):
                listener.exitTypedefType(self)




    def typedefType(self):

        localctx = EnforceParser.TypedefTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_typedefType)
        try:
            self.state = 649
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 647
                self.keyword()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 648
                self.classReference()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(EnforceParser.CLASS, 0)

        def ENUM(self):
            return self.getToken(EnforceParser.ENUM, 0)

        def SWITCH(self):
            return self.getToken(EnforceParser.SWITCH, 0)

        def EXTENDS(self):
            return self.getToken(EnforceParser.EXTENDS, 0)

        def CONST(self):
            return self.getToken(EnforceParser.CONST, 0)

        def BREAK(self):
            return self.getToken(EnforceParser.BREAK, 0)

        def CASE(self):
            return self.getToken(EnforceParser.CASE, 0)

        def ELSE(self):
            return self.getToken(EnforceParser.ELSE, 0)

        def FOR(self):
            return self.getToken(EnforceParser.FOR, 0)

        def CONTINUE(self):
            return self.getToken(EnforceParser.CONTINUE, 0)

        def FOREACH(self):
            return self.getToken(EnforceParser.FOREACH, 0)

        def IF(self):
            return self.getToken(EnforceParser.IF, 0)

        def NEW(self):
            return self.getToken(EnforceParser.NEW, 0)

        def RETURN(self):
            return self.getToken(EnforceParser.RETURN, 0)

        def THIS(self):
            return self.getToken(EnforceParser.THIS, 0)

        def THREAD(self):
            return self.getToken(EnforceParser.THREAD, 0)

        def VOID(self):
            return self.getToken(EnforceParser.VOID, 0)

        def AUTOPTR(self):
            return self.getToken(EnforceParser.AUTOPTR, 0)

        def AUTO(self):
            return self.getToken(EnforceParser.AUTO, 0)

        def REF(self):
            return self.getToken(EnforceParser.REF, 0)

        def NULL(self):
            return self.getToken(EnforceParser.NULL, 0)

        def NOTNULL(self):
            return self.getToken(EnforceParser.NOTNULL, 0)

        def FUNC(self):
            return self.getToken(EnforceParser.FUNC, 0)

        def NATIVE(self):
            return self.getToken(EnforceParser.NATIVE, 0)

        def VOLATILE(self):
            return self.getToken(EnforceParser.VOLATILE, 0)

        def PROTO(self):
            return self.getToken(EnforceParser.PROTO, 0)

        def STATIC(self):
            return self.getToken(EnforceParser.STATIC, 0)

        def OWNED(self):
            return self.getToken(EnforceParser.OWNED, 0)

        def REFERENCE(self):
            return self.getToken(EnforceParser.REFERENCE, 0)

        def OUT(self):
            return self.getToken(EnforceParser.OUT, 0)

        def PROTECTED(self):
            return self.getToken(EnforceParser.PROTECTED, 0)

        def EVENT(self):
            return self.getToken(EnforceParser.EVENT, 0)

        def TYPEDEF(self):
            return self.getToken(EnforceParser.TYPEDEF, 0)

        def MODDED(self):
            return self.getToken(EnforceParser.MODDED, 0)

        def OVERRIDE(self):
            return self.getToken(EnforceParser.OVERRIDE, 0)

        def SEALED(self):
            return self.getToken(EnforceParser.SEALED, 0)

        def INOUT(self):
            return self.getToken(EnforceParser.INOUT, 0)

        def SUPER(self):
            return self.getToken(EnforceParser.SUPER, 0)

        def TYPENAME(self):
            return self.getToken(EnforceParser.TYPENAME, 0)

        def POINTER(self):
            return self.getToken(EnforceParser.POINTER, 0)

        def GOTO(self):
            return self.getToken(EnforceParser.GOTO, 0)

        def PRIVATE(self):
            return self.getToken(EnforceParser.PRIVATE, 0)

        def EXTERNAL(self):
            return self.getToken(EnforceParser.EXTERNAL, 0)

        def DELETE(self):
            return self.getToken(EnforceParser.DELETE, 0)

        def LOCAL(self):
            return self.getToken(EnforceParser.LOCAL, 0)

        def TYPE_INT(self):
            return self.getToken(EnforceParser.TYPE_INT, 0)

        def TYPE_FLOAT(self):
            return self.getToken(EnforceParser.TYPE_FLOAT, 0)

        def TYPE_BOOL(self):
            return self.getToken(EnforceParser.TYPE_BOOL, 0)

        def TYPE_STRING(self):
            return self.getToken(EnforceParser.TYPE_STRING, 0)

        def TYPE_VECTOR(self):
            return self.getToken(EnforceParser.TYPE_VECTOR, 0)

        def LiteralBoolean(self):
            return self.getToken(EnforceParser.LiteralBoolean, 0)

        def DEFAULT(self):
            return self.getToken(EnforceParser.DEFAULT, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword" ):
                listener.enterKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword" ):
                listener.exitKeyword(self)




    def keyword(self):

        localctx = EnforceParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 651
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370494) != 0) or _la==101):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Less(self):
            return self.getToken(EnforceParser.Less, 0)

        def genericType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.GenericTypeContext)
            else:
                return self.getTypedRuleContext(EnforceParser.GenericTypeContext,i)


        def Greater(self):
            return self.getToken(EnforceParser.Greater, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(EnforceParser.Comma)
            else:
                return self.getToken(EnforceParser.Comma, i)

        def getRuleIndex(self):
            return EnforceParser.RULE_typeList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeList" ):
                listener.enterTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeList" ):
                listener.exitTypeList(self)




    def typeList(self):

        localctx = EnforceParser.TypeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_typeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 653
            self.match(EnforceParser.Less)
            self.state = 654
            self.genericType()
            self.state = 659
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==88:
                self.state = 655
                self.match(EnforceParser.Comma)
                self.state = 656
                self.genericType()
                self.state = 661
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 662
            self.match(EnforceParser.Greater)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GenericTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None # ClassReferenceContext

        def classReference(self):
            return self.getTypedRuleContext(EnforceParser.ClassReferenceContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(EnforceParser.VariableModifierContext,i)


        def getRuleIndex(self):
            return EnforceParser.RULE_genericType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGenericType" ):
                listener.enterGenericType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGenericType" ):
                listener.exitGenericType(self)




    def genericType(self):

        localctx = EnforceParser.GenericTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_genericType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39724090916896) != 0):
                self.state = 664
                self.variableModifier()
                self.state = 669
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 670
            localctx.type_ = self.classReference()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GenericTypeDeclarationListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Less(self):
            return self.getToken(EnforceParser.Less, 0)

        def genericTypeDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.GenericTypeDeclarationContext)
            else:
                return self.getTypedRuleContext(EnforceParser.GenericTypeDeclarationContext,i)


        def Greater(self):
            return self.getToken(EnforceParser.Greater, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(EnforceParser.Comma)
            else:
                return self.getToken(EnforceParser.Comma, i)

        def getRuleIndex(self):
            return EnforceParser.RULE_genericTypeDeclarationList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGenericTypeDeclarationList" ):
                listener.enterGenericTypeDeclarationList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGenericTypeDeclarationList" ):
                listener.exitGenericTypeDeclarationList(self)




    def genericTypeDeclarationList(self):

        localctx = EnforceParser.GenericTypeDeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_genericTypeDeclarationList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 672
            self.match(EnforceParser.Less)
            self.state = 673
            self.genericTypeDeclaration()
            self.state = 678
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==88:
                self.state = 674
                self.match(EnforceParser.Comma)
                self.state = 675
                self.genericTypeDeclaration()
                self.state = 680
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 681
            self.match(EnforceParser.Greater)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GenericTypeDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None # ClassReferenceContext
            self.typeName = None # IdentifierContext

        def classReference(self):
            return self.getTypedRuleContext(EnforceParser.ClassReferenceContext,0)


        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnforceParser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(EnforceParser.VariableModifierContext,i)


        def LSBracket(self):
            return self.getToken(EnforceParser.LSBracket, 0)

        def RSBracket(self):
            return self.getToken(EnforceParser.RSBracket, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_genericTypeDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGenericTypeDeclaration" ):
                listener.enterGenericTypeDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGenericTypeDeclaration" ):
                listener.exitGenericTypeDeclaration(self)




    def genericTypeDeclaration(self):

        localctx = EnforceParser.GenericTypeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_genericTypeDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 686
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39724090916896) != 0):
                self.state = 683
                self.variableModifier()
                self.state = 688
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 689
            localctx.type_ = self.classReference()
            self.state = 690
            localctx.typeName = self.identifier()
            self.state = 693
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==92:
                self.state = 691
                self.match(EnforceParser.LSBracket)
                self.state = 692
                self.match(EnforceParser.RSBracket)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSBracket(self):
            return self.getToken(EnforceParser.LSBracket, 0)

        def functionCall(self):
            return self.getTypedRuleContext(EnforceParser.FunctionCallContext,0)


        def RSBracket(self):
            return self.getToken(EnforceParser.RSBracket, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotation" ):
                listener.enterAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotation" ):
                listener.exitAnnotation(self)




    def annotation(self):

        localctx = EnforceParser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_annotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 695
            self.match(EnforceParser.LSBracket)
            self.state = 696
            self.functionCall()
            self.state = 697
            self.match(EnforceParser.RSBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.classname = None # IdentifierContext

        def identifier(self):
            return self.getTypedRuleContext(EnforceParser.IdentifierContext,0)


        def typeList(self):
            return self.getTypedRuleContext(EnforceParser.TypeListContext,0)


        def getRuleIndex(self):
            return EnforceParser.RULE_classReference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassReference" ):
                listener.enterClassReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassReference" ):
                listener.exitClassReference(self)




    def classReference(self):

        localctx = EnforceParser.ClassReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_classReference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 699
            localctx.classname = self.identifier()
            self.state = 701
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
            if la_ == 1:
                self.state = 700
                self.typeList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeftShiftContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Less(self, i:int=None):
            if i is None:
                return self.getTokens(EnforceParser.Less)
            else:
                return self.getToken(EnforceParser.Less, i)

        def getRuleIndex(self):
            return EnforceParser.RULE_leftShift

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeftShift" ):
                listener.enterLeftShift(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeftShift" ):
                listener.exitLeftShift(self)




    def leftShift(self):

        localctx = EnforceParser.LeftShiftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_leftShift)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 703
            self.match(EnforceParser.Less)
            self.state = 704
            self.match(EnforceParser.Less)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RightShiftContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Greater(self, i:int=None):
            if i is None:
                return self.getTokens(EnforceParser.Greater)
            else:
                return self.getToken(EnforceParser.Greater, i)

        def getRuleIndex(self):
            return EnforceParser.RULE_rightShift

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRightShift" ):
                listener.enterRightShift(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRightShift" ):
                listener.exitRightShift(self)




    def rightShift(self):

        localctx = EnforceParser.RightShiftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_rightShift)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.match(EnforceParser.Greater)
            self.state = 707
            self.match(EnforceParser.Greater)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeModiferContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODDED(self):
            return self.getToken(EnforceParser.MODDED, 0)

        def SEALED(self):
            return self.getToken(EnforceParser.SEALED, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_typeModifer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeModifer" ):
                listener.enterTypeModifer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeModifer" ):
                listener.exitTypeModifer(self)




    def typeModifer(self):

        localctx = EnforceParser.TypeModiferContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_typeModifer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 709
            _la = self._input.LA(1)
            if not(_la==34 or _la==36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIVATE(self):
            return self.getToken(EnforceParser.PRIVATE, 0)

        def PROTECTED(self):
            return self.getToken(EnforceParser.PROTECTED, 0)

        def STATIC(self):
            return self.getToken(EnforceParser.STATIC, 0)

        def AUTOPTR(self):
            return self.getToken(EnforceParser.AUTOPTR, 0)

        def PROTO(self):
            return self.getToken(EnforceParser.PROTO, 0)

        def REF(self):
            return self.getToken(EnforceParser.REF, 0)

        def REFERENCE(self):
            return self.getToken(EnforceParser.REFERENCE, 0)

        def CONST(self):
            return self.getToken(EnforceParser.CONST, 0)

        def OWNED(self):
            return self.getToken(EnforceParser.OWNED, 0)

        def OUT(self):
            return self.getToken(EnforceParser.OUT, 0)

        def NOTNULL(self):
            return self.getToken(EnforceParser.NOTNULL, 0)

        def INOUT(self):
            return self.getToken(EnforceParser.INOUT, 0)

        def LOCAL(self):
            return self.getToken(EnforceParser.LOCAL, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_variableModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableModifier" ):
                listener.enterVariableModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableModifier" ):
                listener.exitVariableModifier(self)




    def variableModifier(self):

        localctx = EnforceParser.VariableModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_variableModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 711
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 39724090916896) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIVATE(self):
            return self.getToken(EnforceParser.PRIVATE, 0)

        def EXTERNAL(self):
            return self.getToken(EnforceParser.EXTERNAL, 0)

        def PROTECTED(self):
            return self.getToken(EnforceParser.PROTECTED, 0)

        def STATIC(self):
            return self.getToken(EnforceParser.STATIC, 0)

        def OVERRIDE(self):
            return self.getToken(EnforceParser.OVERRIDE, 0)

        def OWNED(self):
            return self.getToken(EnforceParser.OWNED, 0)

        def REF(self):
            return self.getToken(EnforceParser.REF, 0)

        def REFERENCE(self):
            return self.getToken(EnforceParser.REFERENCE, 0)

        def PROTO(self):
            return self.getToken(EnforceParser.PROTO, 0)

        def NATIVE(self):
            return self.getToken(EnforceParser.NATIVE, 0)

        def VOLATILE(self):
            return self.getToken(EnforceParser.VOLATILE, 0)

        def EVENT(self):
            return self.getToken(EnforceParser.EVENT, 0)

        def getRuleIndex(self):
            return EnforceParser.RULE_functionModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionModifier" ):
                listener.enterFunctionModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionModifier" ):
                listener.exitFunctionModifier(self)




    def functionModifier(self):

        localctx = EnforceParser.FunctionModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_functionModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 713
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 13235999735808) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 11)
         





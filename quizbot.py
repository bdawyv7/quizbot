import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, PollAnswerHandler, ContextTypes

#TOKEN = os.getenv("8042821970:AAHsCv3OoKKf-JkyNzb9-kuJpPpehK-kgbI")



# Quiz data
quiz_data = [
    {
        "question": "In ______ transmission, the channel capacity is shared by both communicating devices at all times",
        "choices": ["half-simplex", "simplex", "half-duplex", "full-duplex"],
        "answer": 3  # full-duplex
    },
    {
        "question": "______ is the protocol suite for the current Internet.",
        "choices": ["UNIX", "TCP/IP", "ACM", "NCP"],
        "answer": 1  # TCP/IP
    },
    {
        "question": "______ refers to the structure or format of the data, meaning the order in which they are presented.",
        "choices": ["Timing", "Syntax", "Semantics", "All of the above"],
        "answer": 1  # Syntax
    },
    {
        "question": "______ defines how a particular pattern to be interpreted, and what action is to be taken based on that interpretation.",
        "choices": ["Syntax", "Semantics", "None of the above", "Timing"],
        "answer": 1  # Semantics
    },
    {
        "question": "______ refers to two characteristics: when data should be sent and how fast it can be sent.",
        "choices": ["Timing", "Syntax", "none of the above", "Semantics"],
        "answer": 0  # Timing
    },
    {
        "question": "Data flow between two devices can occur in a ______ way.",
        "choices": ["half-duplex", "simplex", "all of the above", "full-duplex"],
        "answer": 2  # all of the above
    },
    {
        "question": "In a ______ connection, two and only two devices are connected by a dedicated link.",
        "choices": ["none of the above", "point-to-point", "multipoint", "(a) and (b)"],
        "answer": 1  # point-to-point
    },
    {
        "question": "In a ______ connection, three or more devices share a link.",
        "choices": ["none of the above", "point-to-point", "multipoint", "(a) and (b)"],
        "answer": 2  # multipoint
    },
    {
        "question": "______ refers to the physical or logical arrangement of a network.",
        "choices": ["Topology", "Mode of operation", "None of the above", "Data flow"],
        "answer": 0  # Topology
    },
    {
        "question": "Devices may be arranged in a ______ topology",
        "choices": ["bus", "all of the above", "ring", "mesh"],
        "answer": 1  # all of the above
    },
    {
        "question": "A ______ is a data communication system within a building, plant, or campus, or between nearby buildings.",
        "choices": ["WAN", "none of the above", "LAN", "MAN"],
        "answer": 2  # LAN
    },
    {
        "question": "A ______ is a data communication system spanning states, countries, or the whole world.",
        "choices": ["WAN", "LAN", "none of the above", "MAN"],
        "answer": 0  # WAN
    },
    {
        "question": "______ is a collection of many separate networks.",
        "choices": ["a LAN", "An internet", "None of the above", "A WAN"],
        "answer": 1  # An internet
    },
    {
        "question": "There are ______ Internet service providers.",
        "choices": ["regional", "all of the above", "local", "national and international"],
        "answer": 1  # all of the above
    },
    {
        "question": "A ______ is a set of rules that governs data communication.",
        "choices": ["none of the above", "protocol", "standard", "forum"],
        "answer": 1  # protocol
    },
    {
        "question": "The ______ is the physical path over which a message travels.",
        "choices": ["Signal", "All the above", "Medium", "Protocol"],
        "answer": 2  # Medium
    },
    {
        "question": "The information to be communicated in a data communications system is the ______.",
        "choices": ["Message", "Transmission", "Protocol", "Medium"],
        "answer": 0  # Message
    },
    {
        "question": "Frequency of failure and network recovery time after a failure are measures of the ______ of a network.",
        "choices": ["Security", "Reliability", "Performance", "Feasibility"],
        "answer": 1  # Reliability
    },
    {
        "question": "An unauthorized user is a network ______ issue.",
        "choices": ["Security", "All the above", "Performance", "Reliability"],
        "answer": 0  # Security
    },
    {
        "question": "Which topology requires a central controller or hub?",
        "choices": ["Mesh", "Bus", "Star", "Ring"],
        "answer": 2  # Star
    },
    {
        "question": "Which topology requires a multipoint connection?",
        "choices": ["Bus", "Mesh", "Star", "Ring"],
        "answer": 0  # Bus
    },
    {
        "question": "Communication between a computer and a keyboard involves ______ transmission.",
        "choices": ["full-duplex", "simplex", "automatic", "half-duplex"],
        "answer": 1  # simplex
    },
    {
        "question": "A television broadcast is an example of ______ transmission.",
        "choices": ["simplex", "full-duplex", "automatic", "half-duplex"],
        "answer": 0  # simplex
    },
    {
        "question": "______ connection provides a dedicated link between two devices.",
        "choices": ["secondary", "point-to-point", "primary", "multipoint"],
        "answer": 1  # point-to-point
    },
    {
        "question": "In a ______ connection, more than two devices can share a single link.",
        "choices": ["multipoint", "point-to-point", "secondary", "primary"],
        "answer": 0  # multipoint
    },
    {
        "question": "______ provides a connection-oriented reliable service for sending messages",
        "choices": ["UDP", "All of the above", "IP", "TCP"],
        "answer": 3  # TCP
    },
    {
        "question": "______ is the first layer that interact with user",
        "choices": ["Datalink layer", "Application layer", "Network layer", "Transport layer"],
        "answer": 1  # Application layer
    },
    {
        "question": "______ define data format and provide compression/decompression",
        "choices": ["Presentation layer", "Datalink layer", "Network layer", "Transport layer"],
        "answer": 0  # Presentation layer
    },
    {
        "question": "Set a logical connection between different application",
        "choices": ["session layer", "Datalink layer", "Transport layer", "Network layer"],
        "answer": 0  # session layer
    },
    {
        "question": "______ is responsible for the reliable transfer of data",
        "choices": ["Transport layer", "Application layer", "Datalink layer", "Network layer"],
        "answer": 0  # Transport layer
    },
    {
        "question": "______ Specifies communication mode (simple -Half duplex – full duplex)",
        "choices": ["session layer", "Datalink layer", "Transport layer", "Network layer"],
        "answer": 0  # session layer
    },
    {
        "question": "Transmission Control Protocol (TCP) provide………",
        "choices": ["connection-oriented", "Error Recovery", "ALL of the above", "Flow control (Buffering – windowing)"],
        "answer": 2  # ALL of the above
    },
    {
        "question": "UDP stands for………",
        "choices": ["Transmission Control Protocol", "User Datagram Protocol", "non of the above", "unified datagram protocol"],
        "answer": 1  # User Datagram Protocol
    },
    {
        "question": "______ has the ability to negotiate with the upper layer to identify the addressing mode (IPv4 or IPv6)",
        "choices": ["Network layer", "Transport layer", "session layer", "Datalink layer"],
        "answer": 0  # Network layer
    },
    {
        "question": "we called the data which has been passed from the application layer to transport layer",
        "choices": ["packet", "segment", "data", "frame"],
        "answer": 1  # segment
    },
    {
        "question": "we use the word(frame) to refer to the data in ...... layer.",
        "choices": ["Transport layer", "session layer", "Datalink layer", "Network layer"],
        "answer": 2  # Datalink layer
    },
    {
        "question": "we use the word(packet) to refer to the data in ...... layer",
        "choices": ["Network layer", "Transport layer", "Datalink layer", "session layer"],
        "answer": 0  # Network layer
    },
    {
        "question": "It makes an operation on the payload and gives a hash with the data sends it to the second device.",
        "choices": ["fcc", "fcs", "fsc", "fss"],
        "answer": 1  # fcs
    },
{
        "question": "______ is the protocol suite for the current Internet.",
        "choices": ["TCP/IP", "NCP", "UNIX", "ACM"],
        "answer": 0  # Assuming TCP/IP is correct (index 0)
    },
    {
        "question": "______ refers to the structure or format of the data, meaning the order in which they are presented.",
        "choices": ["Semantics", "Syntax", "Timing", "All of the above"],
        "answer": 1  # Assuming Syntax is correct (index 1)
    },
    {
        "question": "______ refers to two characteristics: when data should be sent and how fast it can be sent.",
        "choices": ["Semantics", "Syntax", "Timing", "None of the above"],
        "answer": 2  # Assuming Timing is correct (index 2)
    },
    {
        "question": "Data flow between two devices can occur in a ______ way.",
        "choices": ["simplex", "half-duplex", "full-duplex", "all of the above"],
        "answer": 3  # Assuming "all of the above" is correct (index 3)
    },
    {
        "question": "The ______ is the physical path over which a message travels.",
        "choices": ["Protocol", "Medium", "Signal", "All the above"],
        "answer": 1  # Assuming Medium is correct (index 1)
    },
    {
        "question": "The information to be communicated in a data communications system is the ______.",
        "choices": ["Medium", "Protocol", "Message", "Transmission"],
        "answer": 2  # Assuming Message is correct (index 2)
    },
    {
        "question": "Frequency of failure and network recovery time after a failure are measures of the ______ of a network.",
        "choices": ["Performance", "Reliability", "Security", "Feasibility"],
        "answer": 1  # Assuming Reliability is correct (index 1)
    },
    {
        "question": "A television broadcast is an example of ______ transmission.",
        "choices": ["simplex", "half-duplex", "full-duplex", "automatic"],
        "answer": 0  # Assuming simplex is correct (index 0)
    },
    {
        "question": "Before data can be transmitted, they must be transformed to ______.",
        "choices": ["periodic signals", "electromagnetic signals", "aperiodic signals", "low-frequency sine waves"],
        "answer": 1  # Assuming electromagnetic signals is correct (index 1)
    },
    {
        "question": "In a frequency-domain plot, the horizontal axis measures the ______.",
        "choices": ["peak amplitude", "frequency", "phase", "slope"],
        "answer": 1  # Assuming frequency is correct (index 1)
    },
    {
        "question": "Given two sine waves A and B, if the frequency of A is twice that of B, then the period of B is ______ that of A.",
        "choices": ["one-half", "twice", "the same as", "indeterminate from"],
        "answer": 1  # Assuming twice is correct (index 1)
    },
    {
        "question": "A sine wave is ______.",
        "choices": ["periodic and continuous", "aperiodic and continuous", "periodic and discrete", "aperiodic and discrete"],
        "answer": 0  # Assuming periodic and continuous is correct (index 0)
    },
    {
        "question": "______ is a type of transmission impairment in which the signal loses strength due to the resistance of the transmission medium.",
        "choices": ["Attenuation", "Distortion", "Noise", "Decibel"],
        "answer": 0  # Assuming Attenuation is correct (index 0)
    },
    {
        "question": "When propagation speed is multiplied by propagation time, we get the ______.",
        "choices": ["throughput", "wavelength of the signal", "distortion factor", "distance a signal or bit has traveled"],
        "answer": 3  # Assuming distance is correct (index 3)
    },
    {
        "question": "______ data have discrete states and take discrete values.",
        "choices": ["Analog", "Digital", "(a) or (b)", "None of the above"],
        "answer": 1  # Assuming Digital is correct (index 1)
    },
    {
        "question": "______ signals can have only a limited number of values.",
        "choices": ["Analog", "Digital", "(a) or (b)", "None of the above"],
        "answer": 1  # Assuming Digital is correct (index 1)
    },
    {
        "question": "Frequency and period are ______.",
        "choices": ["inverse of each other", "proportional to each other", "the same", "none of the above"],
        "answer": 0  # Assuming inverse is correct (index 0)
    },
    {
        "question": "______ is the rate of change with respect to time.",
        "choices": ["Amplitude", "Time", "Frequency", "Voltage"],
        "answer": 2  # Assuming Frequency is correct (index 2)
    },
    {
        "question": "A sine wave in the ______ domain can be represented by one single spike in the ______ domain.",
        "choices": ["time; frequency", "frequency; time", "time; phase", "phase; time"],
        "answer": 0  # Assuming time; frequency is correct (index 0)
    },
    {
        "question": "The ______ of a composite signal is the difference between the highest and the lowest frequencies contained in that signal.",
        "choices": ["frequency", "period", "bandwidth", "amplitude"],
        "answer": 2  # Assuming bandwidth is correct (index 2)
    },
    {
        "question": "A(n) ______ signal is a composite analog signal with an infinite bandwidth.",
        "choices": ["digital", "analog", "either (a) or (b)", "neither (a) nor (b)"],
        "answer": 1  # Assuming analog is correct (index 1)
    },
    {
        "question": "Baseband transmission of a digital signal is possible only if we have a ______ channel.",
        "choices": ["low-pass", "bandpass", "low rate", "high rate"],
        "answer": 0  # Assuming low-pass is correct (index 0)
    },
    {
        "question": "If the available channel is a ______ channel, we cannot send a digital signal directly to the channel.",
        "choices": ["low-pass", "bandpass", "low rate", "high rate"],
        "answer": 1  # Assuming bandpass is correct (index 1)
    },
    {
        "question": "______ can impair a signal.",
        "choices": ["Noise", "Attenuation", "Distortion", "All of the above"],
        "answer": 3  # Assuming All of the above is correct (index 3)
    },
    {
        "question": "For a ______ channel, we need to use the Shannon capacity to find the maximum bit rate.",
        "choices": ["noiseless", "noisy", "low-pass", "bandpass"],
        "answer": 1  # Assuming noisy is correct (index 1)
    },
    {
        "question": "A television broadcast is an example of ______ transmission.",
        "choices": ["simplex", "half-duplex", "full-duplex", "automatic"],
        "answer": 0  # Assuming simplex is correct (index 0)
    },
    {
        "question": "The Internetworking Protocol (IP) is a ______ protocol.",
        "choices": ["reliable", "connection-oriented", "both a and b", "none of the above"],
        "answer": 3  # Assuming none of the above is correct (index 3)
    },
    {
        "question": "______ provides full transport layer services to applications.",
        "choices": ["TCP", "UDP", "ARP", "none of the above"],
        "answer": 0  # Assuming TCP is correct (index 0)
    },
    {
        "question": "Data can be ______.",
        "choices": ["analog", "digital", "(a) or (b)", "none of the above"],
        "answer": 2  # Assuming (a) or (b) is correct (index 2)
    },
    {
        "question": "A ______ digital signal includes timing information in the data being transmitted.",
        "choices": ["self-synchronizing", "self-modulated", "self-transmitted", "none of the above"],
        "answer": 0  # Assuming self-synchronizing is correct (index 0)
    },
    {
        "question": "The data rate is sometimes called the ______ rate.",
        "choices": ["baud", "bit", "signal", "none of the above"],
        "answer": 1  # Assuming bit is correct (index 1)
    },
    {
        "question": "In a ______ scheme, all the signal levels are on one side of the time axis, either above or below.",
        "choices": ["polar", "bipolar", "unipolar", "all of the above"],
        "answer": 2  # Assuming unipolar is correct (index 2)
    },
    {
        "question": "In ______, the level of the voltage determines the value of the bit.",
        "choices": ["NRZ-I", "NRZ-L", "both (a) and (b)", "neither (a) nor (b)"],
        "answer": 1  # Assuming NRZ-L is correct (index 1)
    },
    {
        "question": "In ______, the change or lack of change in the level of the voltage determines the value of the bit.",
        "choices": ["NRZ-I", "NRZ-L", "both (a) and (b)", "neither (a) nor (b)"],
        "answer": 0  # Assuming NRZ-I is correct (index 0)
    },
    {
        "question": "In ______ encoding, we use three levels: positive, zero, and negative.",
        "choices": ["unipolar", "bipolar", "polar", "none of the above"],
        "answer": 1  # Assuming bipolar is correct (index 1)
    },
    {
        "question": "The ______ scheme uses data patterns of size 2 and encodes the 2-bit patterns as one signal element belonging to a four-level signal.",
        "choices": ["4B5B", "2B1Q", "MLT-3", "none of the above"],
        "answer": 1  # Assuming 2B1Q is correct (index 1)
    },
    {
        "question": "Unipolar, bipolar, and polar encoding are types of ______ encoding.",
        "choices": ["line", "block", "NRZ", "Manchester"],
        "answer": 0  # Assuming line is correct (index 0)
    },
    {
        "question": "PCM is an example of ______ conversion.",
        "choices": ["digital-to-digital", "digital-to-analog", "analog-to-analog", "analog-to-digital"],
        "answer": 3  # Assuming analog-to-digital is correct (index 3)
    },
    {
        "question": "Which of the following encoding methods does not provide for synchronization?",
        "choices": ["NRZ-L", "RZ", "NRZ-I", "Manchester"],
        "answer": 0  # Assuming NRZ-L is correct (index 0)
    },
    {
        "question": "______ conversion involves three techniques: line coding, block coding, and scrambling.",
        "choices": ["Analog-to-digital", "Digital-to-analog", "Analog-to-analog", "Digital-to-digital"],
        "answer": 3  # Assuming Digital-to-digital is correct (index 3)
    },
 {
        "question": "______ is the process of converting digital data to a digital signal.",
        "choices": ["Block coding", "Line coding", "Scrambling", "None of the above"],
        "answer": 1
    },
    {
        "question": "The most common technique to change an analog signal to digital data is called______.",
        "choices": ["PAL", "PCM", "sampling", "none of the above"],
        "answer": 1
    },
    {
        "question": "The first step in PCM is ____.",
        "choices": ["quantization", "modulation", "sampling", "none of the above"],
        "answer": 2
    },
    {
        "question": "______ finds the value of the signal amplitude for each sample; ______ finds the change from the previous sample.",
        "choices": ["DM; PCM", "PCM; DM", "DM; CM", "none of the above"],
        "answer": 1
    },
    {
        "question": "Which of the following is not a digital-to-analog conversion?",
        "choices": ["ASK", "PSK", "FSK", "AM"],
        "answer": 3
    },
    {
        "question": "In ______, the amplitude of the carrier signal is varied to create signal elements. Both frequency and phase remain constant.",
        "choices": ["ASK", "PSK", "FSK", "QAM"],
        "answer": 0
    },
    {
        "question": "In ______, the frequency of the carrier signal is varied to represent data. Both peak amplitude and phase remain constant.",
        "choices": ["ASK", "PSK", "FSK", "QAM"],
        "answer": 2
    },
    {
        "question": "______ uses two carriers, one in-phase and the other quadrature.",
        "choices": ["ASK", "PSK", "FSK", "QAM"],
        "answer": 3
    },
    {
        "question": "______ conversion is the representation of analog information by an analog signal.",
        "choices": ["Digital-to-analog", "Analog-to-analog", "Analog-to-digital", "Digital-to-digital"],
        "answer": 1
    },
    {
        "question": "Analog-to-analog conversion is needed if the available bandwidth is ______.",
        "choices": ["low-pass", "band-pass", "either (a) or (b)", "neither (a) nor (b)"],
        "answer": 1
    },
    {
        "question": "Which of the following is not an analog-to-analog conversion?",
        "choices": ["AM", "PM", "FM", "QAM"],
        "answer": 3
    },
    {
        "question": "In ______ transmission, the carrier signal is modulated so that its amplitude varies with the changing amplitudes of the modulating signal.",
        "choices": ["AM", "PM", "FM", "none of the above"],
        "answer": 0
    },
    {
        "question": "In ______ transmission, the phase of the carrier signal is modulated to follow the changing voltage level (amplitude) of the modulating signal.",
        "choices": ["AM", "PM", "FM", "none of the above"],
        "answer": 1
    },
    {
        "question": "In ______, the peak amplitude of one signal level is 0; the other is the same as the amplitude of the carrier frequency.",
        "choices": ["PSK", "OOK", "FSK", "none of the above"],
        "answer": 1
    },
    {
        "question": "ASK, PSK, FSK, and QAM are examples of ______ conversion.",
        "choices": ["digital-to-digital", "digital-to-analog", "analog-to-analog", "analog-to-digital"],
        "answer": 1
    },
    {
        "question": "AM and FM are examples of ______ conversion.",
        "choices": ["digital-to-digital", "digital-to-analog", "analog-to-analog", "analog-to-digital"],
        "answer": 2
    },
    {
        "question": "In QAM, both ______ of a carrier frequency are varied.",
        "choices": ["frequency and amplitude", "phase and frequency", "amplitude and phase", "none of the above"],
        "answer": 2
    },
    {
        "question": "In a multiplexed system, ______ lines share the bandwidth of ______ link.",
        "choices": ["1; n", "1; 1", "n; 1", "n; n"],
        "answer": 2
    },
    {
        "question": "The word ______ refers to the portion of a ______ that carries a transmission.",
        "choices": ["channel; link", "link; channel", "line; channel", "line; link"],
        "answer": 0
    },
    {
        "question": "______ can be applied when the bandwidth of a link (in hertz) is greater than the combined bandwidths of the signals to be transmitted.",
        "choices": ["TDM", "FDM", "Both (a) or (b)", "Neither (a) or (b)"],
        "answer": 1
    },
    {
        "question": "FSM is an ______ technique.",
        "choices": ["analog", "digital", "either (a) or (b)", "none of the above"],
        "answer": 1
    },
    {
        "question": "______ is designed to use the high bandwidth capability of fiber-optic cable.",
        "choices": ["FDM", "TDM", "WDM", "None of the above"],
        "answer": 2
    },
    {
        "question": "______ is a digital process that allows several connections to share the high bandwidth of a link.",
        "choices": ["FDM", "TDM", "WDM", "None of the above"],
        "answer": 1
    },
    {
        "question": "______ is a digital multiplexing technique for combining several low-rate channels into one high-rate one.",
        "choices": ["FDM", "TDM", "WDM", "None of the above"],
        "answer": 1
    },
    {
        "question": "We can divide ______ into two different schemes: synchronous or statistical.",
        "choices": ["FDM", "TDM", "WDM", "none of the above"],
        "answer": 1
    },
    {
        "question": "Which multiplexing technique transmits analog signals?",
        "choices": ["FDM", "TDM", "WDM", "(a) and (c)"],
        "answer": 3
    },
    {
        "question": "Which multiplexing technique shifts each signal to a different carrier frequency?",
        "choices": ["FDM", "TDM", "Both (a) and (b)", "None of the above"],
        "answer": 0
    },
    {
        "question": "______ cable consists of two insulated copper wires twisted together.",
        "choices": ["Coaxial", "Fiber-optic", "Twisted-pair", "none of the above"],
        "answer": 2
    },
    {
        "question": "______ cable is used for voice and data communications.",
        "choices": ["Coaxial", "Fiber-optic", "Twisted-pair", "none of the above"],
        "answer": 2
    },
    {
        "question": "______ cables are composed of a glass or plastic inner core surrounded by cladding, all encased in an outside jacket.",
        "choices": ["Coaxial", "Fiber-optic", "Twisted-pair", "none of the above"],
        "answer": 1
    },
    {
        "question": "In a fiber-optic cable, the signal is propagated along the inner core by ______.",
        "choices": ["reflection", "refraction", "modulation", "none of the above"],
        "answer": 0
    },
    {
        "question": "In fiber optics, the signal is ______ waves.",
        "choices": ["light", "radio", "infrared", "very low-frequency"],
        "answer": 0
    },
    {
        "question": "Which of the following is not a guided medium?",
        "choices": ["twisted-pair cable", "coaxial cable", "fiber-optic cable", "atmosphere"],
        "answer": 3
    },
    {
        "question": "A ______ network is a cross between a circuit-switched network and a datagram network. It has some characteristics of both.",
        "choices": ["virtual-circuit", "packet-switched", "frame-switched", "none of the above"],
        "answer": 0
    },
    {
        "question": "The simplest type of switching fabric is the ______ switch.",
        "choices": ["crosspoint", "crossbar", "TSI", "STS"],
        "answer": 1
    },
    {
        "question": "A ______ switch is a multistage switch with microswitches at each stage that route the packets based on the output port represented as a binary string.",
        "choices": ["crossbar", "TSI", "banyan", "none of the above"],
        "answer": 2
    },
    {
        "question": "The most popular technology in time-division switching is called the ______.",
        "choices": ["STI", "ITS", "TSI", "none of the above"],
        "answer": 2
    },
    {
        "question": "A switched WAN is normally implemented as a ______ network.",
        "choices": ["virtual-circuit", "datagram", "circuit-switched", "none of the above"],
        "answer": 0
    },
    {
        "question": "In a ______ network, two types of addressing are involved: global and local.",
        "choices": ["virtual-circuit", "datagram", "circuit-switched", "none of the above"],
        "answer": 0
    },
    {
        "question": "Circuit switching takes place at the ______ layer.",
        "choices": ["data line", "physical", "network", "transport"],
        "answer": 1
    },
    {
        "question": "In ______, there is no resource allocation for a packet.",
        "choices": ["datagram switching", "circuit switching", "frame switching", "none of the above"],
        "answer": 0
    },
    {
        "question": "The ______ layer changes bits onto electromagnetic signals.",
        "choices": ["Physical", "Transport", "Data Link", "Presentation"],
        "answer": 0
    },
    {
        "question": "The loss in signal power as light travels down the fiber is called ______.",
        "choices": ["Attenuation", "Propagation", "Scattering", "Interruption"],
        "answer": 0
    },
    {
        "question": "On which factor/s do/does the channel capacity depend/s in the communication system?",
        "choices": ["Bandwidth", "Signal to Noise Ratio", "Both a and b", "None of the above"],
        "answer": 2
    },
{
        "question": "Before data can be transmitted, they must be transformed to ______.",
        "choices": ["periodic signals", "electromagnetic signals", "aperiodic signals", "low-frequency sine waves"],
        "answer": 1  # Assuming "electromagnetic signals" is pink-highlighted (index 1)
    },
    {
        "question": "A periodic signal completes one cycle in 0.001 s. What is the frequency?",
        "choices": ["1 Hz", "100 Hz", "1 KHz", "1 MHz"],
        "answer": 2  # Assuming "1 KHz" is correct (index 2)
    },
    {
        "question": "In a frequency-domain plot, the horizontal axis measures the ______.",
        "choices": ["peak amplitude", "frequency", "phase", "slope"],
        "answer": 1  # Assuming "frequency" is correct (index 1)
    },
    {
        "question": "In a time-domain plot, the horizontal axis is a measure of ______.",
        "choices": ["signal amplitude", "frequency", "phase", "time"],
        "answer": 3  # Assuming "time" is correct (index 3)
    },
    {
        "question": "If the bandwidth of a signal is 5 KHz and the lowest frequency is 52 KHz, what is the highest frequency?",
        "choices": ["5 KHz", "10 KHz", "47 KHz", "57 KHz"],
        "answer": 3  # Assuming "57 KHz" is correct (index 3)
    },
    {
        "question": "What is the bandwidth of a signal that ranges from 1 MHz to 4 MHz?",
        "choices": ["4 MHz", "1 KHz", "3 MHz", "none of the above"],
        "answer": 2  # Assuming "3 MHz" is correct (index 2)
    },
    {
        "question": "As frequency increases, the period ______.",
        "choices": ["decreases", "increases", "remains the same", "doubles"],
        "answer": 0  # Assuming "decreases" is correct (index 0)
    },
    {
        "question": "Given two sine waves A and B, if the frequency of A is twice that of B, then the period of B is ______ that of A.",
        "choices": ["one-half", "twice", "the same as", "indeterminate from"],
        "answer": 1  # Assuming "twice" is correct (index 1)
    },
    {
        "question": "A sine wave is ______.",
        "choices": ["periodic and continuous", "aperiodic and continuous", "periodic and discrete", "aperiodic and discrete"],
        "answer": 0  # Assuming "periodic and continuous" is correct (index 0)
    },
    {
        "question": "If the maximum amplitude of a sine wave is 2 V, the minimum amplitude is ______.",
        "choices": ["2", "1", "-2", "between -2 and 2"],
        "answer": 2  # Assuming "-2" is correct (index 2)
    },
    {
        "question": "A signal is measured at two different points. The power is P1 at the first point and P2 at the second point. The dB is 0. This means ______.",
        "choices": ["P2 is zero", "P2 equals P1", "P2 is much larger than P1", "P2 is much smaller than P1"],
        "answer": 1  # Assuming "P2 equals P1" is correct (index 1)
    },
    {
        "question": "______ is a type of transmission impairment in which the signal loses strength due to the resistance of the transmission medium.",
        "choices": ["Attenuation", "Distortion", "Noise", "Decibel"],
        "answer": 0  # Assuming "Attenuation" is correct (index 0)
    },
    {
        "question": "______ is a type of transmission impairment in which the signal loses strength due to the different propagation speeds of each frequency that makes up the signal.",
        "choices": ["Attenuation", "Distortion", "Noise", "Decibel"],
        "answer": 1  # Assuming "Distortion" is correct (index 1)
    },
    {
        "question": "______ is a type of transmission impairment in which an outside source such as crosstalk corrupts a signal.",
        "choices": ["Attenuation", "Distortion", "Noise", "Decibel"],
        "answer": 2  # Assuming "Noise" is correct (index 2)
    },
    {
        "question": "When propagation speed is multiplied by propagation time, we get the ______.",
        "choices": ["throughput", "wavelength of the signal", "distortion factor", "distance a signal or bit has traveled"],
        "answer": 3  # Assuming "distance a signal or bit has traveled" is correct (index 3)
    },
    {
        "question": "Data can be ______.",
        "choices": ["analog", "digital", "(a) or (b)", "none of the above"],
        "answer": 2  # Assuming "(a) or (b)" is correct (index 2)
    },
    {
        "question": "______ data are continuous and take continuous values.",
        "choices": ["analog", "digital", "(a) or (b)", "none of the above"],
        "answer": 0  # Assuming "analog" is correct (index 0)
    },
    {
        "question": "______ data have discrete states and take discrete values.",
        "choices": ["Analog", "Digital", "(a) or (b)", "None of the above"],
        "answer": 1  # Assuming "Digital" is correct (index 1)
    },
    {
        "question": "Signals can be ______.",
        "choices": ["analog", "digital", "either (a) or (b)", "neither (a) nor (b)"],
        "answer": 2  # Assuming "either (a) or (b)" is correct (index 2)
    },
    {
        "question": "______ signals can have an infinite number of values in a range.",
        "choices": ["Analog", "Digital", "(a) or (b)", "None of the above"],
        "answer": 0  # Assuming "Analog" is correct (index 0)
    },
    {
        "question": "______ signals can have only a limited number of values.",
        "choices": ["Analog", "Digital", "(a) or (b)", "None of the above"],
        "answer": 1  # Assuming "Digital" is correct (index 1)
    },
    {
        "question": "Frequency and period are ______.",
        "choices": ["inverse of each other", "proportional to each other", "the same", "none of the above"],
        "answer": 0  # Assuming "inverse of each other" is correct (index 0)
    },
    {
        "question": "______ is the rate of change with respect to time.",
        "choices": ["Amplitude", "Time", "Frequency", "Voltage"],
        "answer": 2  # Assuming "Frequency" is correct (index 2)
    },
    {
        "question": "______ describes the position of the waveform relative to time 0.",
        "choices": ["Frequency", "Phase", "Amplitude", "Voltage"],
        "answer": 1  # Assuming "Phase" is correct (index 1)
    },
    {
        "question": "A sine wave in the ______ domain can be represented by one single spike in the ______ domain.",
        "choices": ["time; frequency", "frequency; time", "time; phase", "phase; time"],
        "answer": 0  # Assuming "time; frequency" is correct (index 0)
    },
    {
        "question": "A ______ sine wave is not useful in data communications; we need to send a ______ signal.",
        "choices": ["composite; single-frequency", "single-frequency; composite", "single-frequency; double-frequency", "none of the above"],
        "answer": 1  # Assuming "single-frequency; composite" is correct (index 1)
    },
    {
        "question": "The ______ of a composite signal is the difference between the highest and the lowest frequencies contained in that signal.",
        "choices": ["frequency", "period", "bandwidth", "amplitude"],
        "answer": 2  # Assuming "bandwidth" is correct (index 2)
    },
    {
        "question": "A(n)______ signal is a composite analog signal with an infinite bandwidth.",
        "choices": ["digital", "analog", "either (a) or (b)", "neither (a) nor (b)"],
        "answer": 1  # Assuming "analog" is correct (index 1)
    },
    {
        "question": "Baseband transmission of a digital signal is possible only if we have a ______ channel.",
        "choices": ["low-pass", "bandpass", "low rate", "high rate"],
        "answer": 0  # Assuming "low-pass" is correct (index 0)
    },
    {
        "question": "If the available channel is a ______ channel, we cannot send a digital signal directly to the channel.",
        "choices": ["low-pass", "bandpass", "low rate", "high rate"],
        "answer": 1  # Assuming "bandpass" is correct (index 1)
    },
    {
        "question": "The black and white TV is an example of ______.",
        "choices": ["non periodic composite signal", "periodic composite signal", "periodic simple signal", "non periodic simple signal"],
        "answer": 1  # Assuming "periodic composite signal" is correct (index 1)
    },
    {
        "question": "______ can impair a signal.",
        "choices": ["Noise", "Attenuation", "Distortion", "All of the above"],
        "answer": 3  # Assuming "All of the above" is correct (index 3)
    },
    {
        "question": "The ______ product defines the number of bits that can fill the link.",
        "choices": ["delay-amplitude", "frequency-amplitude", "bandwidth-period", "bandwidth-delay"],
        "answer": 3  # Assuming "bandwidth-delay" is correct (index 3)
    },
    {
        "question": "For a ______ channel, we need to use the Shannon capacity to find the maximum bit rate.",
        "choices": ["noiseless", "noisy", "low-pass", "bandpass"],
        "answer": 1  # Assuming "noisy" is correct (index 1)
    },
{
        "question": "A network that needs human beings to manually route signals is called....",
        "choices": ["Fiber Optic Network", "Bus Network", "T-switched network", "Ring network"],
        "answer": 2  # Assuming "T-switched network" is correct (index 2)
    },
    {
        "question": "FDDI used which type of physical topology?",
        "choices": ["Bus", "Ring", "Star", "Tree"],
        "answer": 1  # Assuming "Ring" is correct (index 1)
    },
    {
        "question": "FTP stands for",
        "choices": ["File transfer protocol", "File transmission protocol", "Form transfer protocol", "Form transmission protocol"],
        "answer": 0  # Assuming "File transfer protocol" is correct (index 0)
    },
    {
        "question": "Ethernet system uses which of the following technology.",
        "choices": ["Bus", "Ring", "Star", "Tree"],
        "answer": 0  # Assuming "Bus" is correct (index 0)
    },
    {
        "question": "Which of the following are the network services?",
        "choices": ["File service", "Print service", "Database service", "All of the above"],
        "answer": 3  # Assuming "All of the above" is correct (index 3)
    },
    {
        "question": "If all devices are connected to a central hub, then topology is called",
        "choices": ["Bus Topology", "Ring Topology", "Star Topology", "Tree Topology"],
        "answer": 2  # Assuming "Star Topology" is correct (index 2)
    },
    {
        "question": "FDDI stands for",
        "choices": ["Fiber Distributed Data Interface", "Fiber Data Distributed Interface", "Fiber Dual Distributed Interface", "Fiber Distributed Data Interface"],
        "answer": 0  # Assuming first option is correct (index 0)
    },
    {
        "question": "Which of the following is an application layer service?",
        "choices": ["Network virtual terminal", "File transfer, access and management", "Mail service", "All of the above"],
        "answer": 3  # Assuming "All of the above" is correct (index 3)
    },
    {
        "question": "The...... layer change bits onto electromagnetic signals.",
        "choices": ["Physical", "Transport", "Data Link", "Presentation"],
        "answer": 0  # Assuming "Physical" is correct (index 0)
    },
    {
        "question": "In mesh topology, relationship between one device and another is ......",
        "choices": ["Primary to peer", "Peer to primary", "Primary to secondary", "Peer to Peer"],
        "answer": 3  # Assuming "Peer to Peer" is correct (index 3)
    },
    {
        "question": "The performance of data communications network depends on ……….",
        "choices": ["Number of users", "The hardware and software", "The transmission", "All of the above"],
        "answer": 3  # Assuming "All of the above" is correct (index 3)
    },
    {
        "question": "Find out the OSI layer, which performs token management.",
        "choices": ["Network Layer", "Transport Layer", "Session Layer", "Presentation Layer"],
        "answer": 2  # Assuming "Session Layer" is correct (index 2)
    },
    {
        "question": "The name of the protocol which provides virtual terminal in TCP/IP model is.",
        "choices": ["Telnet", "SMTP", "HTTP"],
        "answer": 0  # Assuming "Telnet" is correct (index 0)
    },
    {
        "question": "The layer one of the OSI model is",
        "choices": ["Physical layer", "Link layer", "Router layer", "Broadcast layer"],
        "answer": 0  # Assuming "Physical layer" is correct (index 0)
    },
    {
        "question": "What is the name of the network topology in which there are bi-directional links between each possible node?",
        "choices": ["Ring", "Star", "Tree", "Mesh"],
        "answer": 3  # Assuming "Mesh" is correct (index 3)
    },
    {
        "question": "What is the commonly used unit for measuring the speed of data transmission?",
        "choices": ["Bytes per second", "Baud", "Bits per second", "Both B and C"],
        "answer": 3  # Assuming "Both B and C" is correct (index 3)
    },
    {
        "question": "Which of the communication modes support two way traffic but in only once direction of a time?",
        "choices": ["Simplex", "Half-duplex", "Three - quarter's duplex", "Full duplex"],
        "answer": 1  # Assuming "Half-duplex" is correct (index 1)
    },
    {
        "question": "The loss in signal power as light travels down the fiber is called ……….",
        "choices": ["Attenuation", "Propagation", "Scattering", "Interruption"],
        "answer": 0  # Assuming "Attenuation" is correct (index 0)
    },
    {
        "question": "Which of the following TCP/IP protocols is used for transferring files form one machine to another.",
        "choices": ["FTP", "SNMP", "SMTP", "RPC"],
        "answer": 0  # Assuming "FTP" is correct (index 0)
    },
    {
        "question": "For n devices in a network, what is the number of cable links required for a mesh topology?",
        "choices": ["n (n - 1) / 2", "n", "n-1", "one backbone and n drop lines"],
        "answer": 0  # Assuming "n (n - 1) / 2" is correct (index 0)
    },
    {
        "question": "For n devices in a network, what is the number of cable links required for a Ring topology?",
        "choices": ["n (n - 1) / 2", "n", "n-1", "one backbone and n drop lines"],
        "answer": 1  # Assuming "n" is correct (index 1)
    },
    {
        "question": "For n devices in a network, what is the number of cable links required for a star topology?",
        "choices": ["n (n - 1) / 2", "n", "n-1", "one backbone and n drop lines"],
        "answer": 2  # Assuming "n-1" is correct (index 2)
    },
    {
        "question": "For n devices in a network, what is the number of cable links required for a Bus topology?",
        "choices": ["n (n - 1) / 2", "n", "n-1", "one backbone and n drop lines"],
        "answer": 3  # Assuming "one backbone and n drop lines" is correct (index 3)
    },
    {
        "question": "What is advantage for Mesh topology?",
        "choices": ["secure", "easy installation", "robust", "easy fault isolation"],
        "answer": 2  # Assuming "robust" is correct (index 2)
    },
    {
        "question": "What is advantage for Star topology?",
        "choices": ["secure", "easy installation", "robust", "easy fault isolation"],
        "answer": 1  # Assuming "easy installation" is correct (index 1)
    },
    {
        "question": "What is advantage for Ring topology?",
        "choices": ["secure", "easy installation", "robust", "easy fault isolation"],
        "answer": 0  # Assuming "secure" is correct (index 0)
    },
    {
        "question": "What is advantage for Bus topology?",
        "choices": ["secure", "easy installation", "robust", "easy fault isolation"],
        "answer": 1  # Assuming "easy installation" is correct (index 1)
    },
    {
        "question": "What are some of the factors that determine whether a communication system is a LAN or WAN?",
        "choices": ["size and distances", "structure", "ownership", "All of the above"],
        "answer": 3  # Assuming "All of the above" is correct (index 3)
    },
    {
        "question": "Which of the transport layer protocols is connectionless?",
        "choices": ["UDP", "TCP", "FTP", "Nvt"],
        "answer": 0  # Assuming "UDP" is correct (index 0)
    },
    {
        "question": "Which of the following applications allows a user to access and change remote files without actual transfer?",
        "choices": ["DNS", "FTP", "NFS", "Telnet"],
        "answer": 2  # Assuming "NFS" is correct (index 2)
    },
    {
        "question": "The data unit in the TCP/IP layer called a …..",
        "choices": ["Message", "Segment", "Datagram", "Frame"],
        "answer": 2  # Assuming "Datagram" is correct (index 2)
    },
    {
        "question": "DNS can obtain the ………………of host if its domain name is known and vice versa.",
        "choices": ["Station address", "IP address", "Port address", "Checksum"],
        "answer": 1  # Assuming "IP address" is correct (index 1)
    },
    {
        "question": "Which of the following OSI layers correspond to TCP/IP's application layer?",
        "choices": ["Application", "IP Address", "Session", "All of the above"],
        "answer": 3  # Assuming "All of the above" is correct (index 3)
    },
    {
        "question": "Devices on one network can communicate with devices on another network via a ………",
        "choices": ["File Server", "Utility Server", "Printer Server", "Gateway"],
        "answer": 3  # Assuming "Gateway" is correct (index 3)
    },
    {
        "question": "A communication device that combines transmissions from several I/O devices into one line is a",
        "choices": ["Concentrator", "Modifier", "Multiplexer", "Full duplex file"],
        "answer": 2  # Assuming "Multiplexer" is correct (index 2)
    },
    {
        "question": "Which layers of the OSI determines the interface often system with the user?",
        "choices": ["Network", "Application", "Data link", "Session"],
        "answer": 1  # Assuming "Application" is correct (index 1)
    },
    {
        "question": "In which OSI layers does the FDDI protocol operate?",
        "choices": ["Physical", "Data link", "Network", "A and B"],
        "answer": 3  # Assuming "A and B" is correct (index 3)
    },
    {
        "question": "The………… layer of OSI model can use the trailer of the frame for error detection.",
        "choices": ["Physical", "Data link", "Transport", "Presentation"],
        "answer": 1  # Assuming "Data link" is correct (index 1)
    },
    {
        "question": "The standard suit of protocols used by the Internet, Intranets, extranets and some other networks.",
        "choices": ["TCP/IP", "Protocol", "Open system", "Internet work processor"],
        "answer": 0  # Assuming "TCP/IP" is correct (index 0)
    },
    {
        "question": "State whether the following is True or False. i) In bus topology, heavy Network traffic slows down the bus speed. ii) It is multipoint configuration.",
        "choices": ["True, True", "True, False", "False, True", "False, False"],
        "answer": 0  # Assuming "True, True" is correct (index 0)
    },
    {
        "question": "Which of the following is the logical topology?",
        "choices": ["Bus", "Tree", "Star", "Both A and B"],
        "answer": 3  # Assuming "Both A and B" is correct (index 3)
    },
    {
        "question": "On which factor/s do/does the channel capacity depend/s in the communication system?",
        "choices": ["Bandwidth", "Signal to Noise Ratio", "Both a and b", "None of the above"],
        "answer": 2  # Assuming "Both a and b" is correct (index 2)
    },
    {
        "question": "Which layer determines the data rate for transmission?",
        "choices": ["Physical layer", "network layer", "application layer", "Transport layer"],
        "answer": 0  # Assuming "Physical layer" is correct (index 0)
    },
    {
        "question": "Communication channel having---types.",
        "choices": ["1", "2", "3", "4"],
        "answer": 1  # Assuming "2" is correct (index 1)
    },
    {
        "question": "Frequency of failure and network recovery time after a failure are measures of the ---of a network.",
        "choices": ["Performance", "Security", "Feasibility", "Reliability"],
        "answer": 3  # Assuming "Reliability" is correct (index 3)
    },
    {
        "question": "A television broadcast is an example of---transmission.",
        "choices": ["half-duplex", "simplex", "full-duplex", "automatic"],
        "answer": 1  # Assuming "simplex" is correct (index 1)
    },
    {
        "question": "--- refers to two characteristics: when data should be sent and how fast it can be sent.",
        "choices": ["Semantics", "Syntax", "Timing", "none of the above"],
        "answer": 2  # Assuming "Timing" is correct (index 2)
    },
    {
        "question": "The propagation speed of electromagnetic signals depends on the",
        "choices": ["medium", "period", "phase", "delay"],
        "answer": 0  # Assuming "medium" is correct (index 0)
    },
    {
        "question": "the range of frequencies a channel can pass is called bandwidth in",
        "choices": ["bits per second", "Hertz", "kilogram", "nanosecond"],
        "answer": 1  # Assuming "Hertz" is correct (index 1)
    },
    {
        "question": "When there is heavy traffic on the network, the queuing time is",
        "choices": ["zero", "remains same", "increases", "decreases"],
        "answer": 2  # Assuming "increases" is correct (index 2)
    },
    {
        "question": "The time required for a bit to travel from source to destination is known as",
        "choices": ["latency", "propagation time", "delay", "transmission time"],
        "answer": 1  # Assuming "propagation time" is correct (index 1)
    },
    {
        "question": "The data rate depends upon",
        "choices": ["bandwidth", "level of signals", "level of noise", "all of above"],
        "answer": 3  # Assuming "all of above" is correct (index 3)
    },
    {
        "question": "Multi-level multiplexing, multiple-slot allocation, and pulse stuffing techniques are used to improve……",
        "choices": ["Time Division Multiplexing", "data rate management", "Interleaving", "nothing"],
        "answer": 0  # Assuming "Time Division Multiplexing" is correct (index 0)
    },
    {
        "question": "………gives the frequency domain of a periodic signal",
        "choices": ["Fourier series", "Fourier analysis", "Nyquist theorem"],
        "answer": 0  # Assuming "Fourier series" is correct (index 0)
    },
    {
        "question": "……… gives the frequency domain of a nonperiodic signal.",
        "choices": ["Fourier series", "Fourier analysis", "Nyquist theorem"],
        "answer": 1  # Assuming "Fourier analysis" is correct (index 1)
    },
    {
        "question": "A signal is ……… if its frequency domain plot is discrete;",
        "choices": ["periodic", "nonperiodic", "all of the above", "non"],
        "answer": 0  # Assuming "periodic" is correct (index 0)
    },
    {
        "question": "A signal ………if its frequency domain plot is continuous.",
        "choices": ["periodic", "nonperiodic", "all of the above", "non"],
        "answer": 1  # Assuming "nonperiodic" is correct (index 1)
    },
    {
        "question": "The …. defines the number of data elements (bits) sent in 1s. The unit is bits per second (bps).",
        "choices": ["data rate", "signal rate", "data element", "signal element"],
        "answer": 0  # Assuming "data rate" is correct (index 0)
    },
    {
        "question": "The ……… is the number of signal elements sent in 1s. The unit is the baud.",
        "choices": ["data rate", "signal rate", "data element", "signal element"],
        "answer": 1  # Assuming "signal rate" is correct (index 1)
    },
    {
        "question": "The required bit rate in the baseband transmission is proportional to the",
        "choices": ["Frequency", "Bandwidth", "Phase", "Time-period"],
        "answer": 1  # Assuming "Bandwidth" is correct (index 1)
    },
    {
        "question": "The digital signals cannot be transmitted directly to the channel, when the channel is",
        "choices": ["High-pass", "Baseband", "Bandpass", "Low-pass"],
        "answer": 2  # Assuming "Bandpass" is correct (index 2)
    },
    {
        "question": "Increased number the levels of a signal can result in reduction of",
        "choices": ["Flexibility", "Reliability", "Efficiency", "Effectivity"],
        "answer": 1  # Assuming "Reliability" is correct (index 1)
    },
    {
        "question": "The SNR (signal to noise ratio) can be measured with respect to",
        "choices": ["Avg frequency /Avg noise power", "Avg distortion amount /Avg noise power", "Avg attenuation /Avg noise power", "Avg signal power/Avg noise power"],
        "answer": 3  # Assuming "Avg signal power/Avg noise power" is correct (index 3)
    },
    {
        "question": "A signal with high energy in a very short time, refers to the form of transmission impairment named as :",
        "choices": ["Thermal Noise", "Impulse Noise", "Induced noise", "Cross-talk"],
        "answer": 1  # Assuming "Impulse Noise" is correct (index 1)
    } 
]

# Track user progress
user_data = {}

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_data[user_id] = {"index": 0, "score": 0}
    await send_quiz(update.effective_chat.id, context, user_id)

# Send quiz question
async def send_quiz(chat_id, context: ContextTypes.DEFAULT_TYPE, user_id):
    index = user_data[user_id]["index"]

    if index < len(quiz_data):
        question = quiz_data[index]
        await context.bot.send_poll(
            chat_id=chat_id,
            question=f"Q{index+1}: {question['question']}",
            options=question["choices"],
            type='quiz',
            correct_option_id=question["answer"],
            is_anonymous=False
        )
    else:
        score = user_data[user_id]["score"]
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"✅ Quiz finished!\nYour score: {score}/{len(quiz_data)}"
        )
        del user_data[user_id]

# Handle quiz answer
async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    poll_answer = update.poll_answer
    user_id = poll_answer.user.id
    selected = poll_answer.option_ids[0]

    if user_id in user_data:
        index = user_data[user_id]["index"]
        correct = quiz_data[index]["answer"]

        if selected == correct:
            user_data[user_id]["score"] += 1

        user_data[user_id]["index"] += 1
        await send_quiz(user_id, context, user_id)

# Replace with your actual token
TOKEN = "8042821970:AAHsCv3OoKKf-JkyNzb9-kuJpPpehK-kgbI"


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(PollAnswerHandler(handle_poll_answer))

print("🤖 Bot is running...")
app.run_polling()

const portfolio_data = [
  {
    "title": "Ethereum Decentralized Exchange",
    "header": "Designing a more efficient blockchain decentralized exchange",
      "description":
          `
          Together with Dawn Song's Research team out of UC Berkeley, I worked towards designing a
          more rapid decentralized exchange. This project fundamentally relied
          on integrating state-channels to prevent frequent updates "on chain"
          
          `
  },
  {
   "title": "Platform Engineering With Raydiant Oxymetry",
      "header": "Raydiant Oximetry, Fetal Pulse Oximetry",
      "description": "Beginning Fall 2016, I have been working with\n" +
      "                                Raydiant Oximetry and the Citris Bantao Institute\n" +
      "                                to develop a real-time fetal pulse\n" +
      "                                monitoring system. Building off the communication\n" +
      "                                protocols for our monitoring devices,\n" +
      "                                I built a system to constantly read and process\n" +
      "                                data using a proprietary signal processing algorithm."

  },
  {
    "title": "NP-Complete Approximation",
      "header": "Designing an NP-Complete Approximation Algorithm using Simulated Annealing",
      "description":"We sought to solve a variant of a betweenness problem (a proven NP-Complete Problem)\n" +
      "                                Basically, we were given a series of constraints of the form A B C\n" +
      "                                (which indicates C cannot lie between A and B) and tried to find the optimal\n" +
      "                                ordering such that no constraint was violated. Our approach used simulated annealing\n" +
      "                                and made random swaps to try to improve a cost function defined by constraints violated.\n" +
      "                                There are also quite a few performance enhancements including multithreading, etc.\n" +
      "                                The complete code is <a href=\"https://github.com/Sharabesh/NP-Complete_Solution\">here</a>"
  },
  {
    "title": "Python Recursive Art",
      "header": "Recursive Art Using the Python Turtle Module",
      "description": "Using the Python Turtle Graphics Module to Design recursion based art.\n" +
      "                                Designed for a competition out of UC Berkeley's CS61A course (2nd place).",
  },
  {
    "title": "Analytics Platform Development",
      "header":"Designing a system for analytics into team behavior",
      "description":"As a subsidiary assignment while at Cisco Systems, I worked\n" +
      "                                on designing a user-friendly tool to voice complaints and\n" +
      "                                generate some quick analytics for internal use.\n" +
      "                                This project won the local summer design competition.\n" +
      "                                The code is all <a href=\"https://github.com/Sharabesh/InternCorner\">Here</a>\n" +
      "                                and you can actually visit the site (live on Heroku) <a href=\"https://internbridge.herokuapp.com/\">Website</a>"
  },
  {
    "title": "Alpha-beta pruning with game trees",
      "header":"Optimizing AI decision making",
      "description":"As part of a java-based implementation\n" +
      "                                of Ataxx (a board game similar to chess)\n" +
      "                                I worked on developing an AI for players to\n" +
      "                                compete against.\n" +
      "                                To allow the AI to evaluate possibilities several moves in\n" +
      "                                advance of the current position, I worked\n" +
      "                                on integrating alpha-beta pruning on the generated game-trees to optimize\n" +
      "                                AI response speed"

  },
  {
    "title": "Javascript Graphics",
      "header":"Implementing JavaScript Graphics to show regions of Neural Activation",
      "description":"Used machine-parsed neuroimaging activation\n" +
      "                                data to map activation patterns onto 3D\n" +
      "                                interactive coordinate system. Data is accumulated from hundreds of articles\n" +
      "                                and thresholded to yield specific regions most often corresponding to\n" +
      "                                the particular keyword query."
  },
  {
    "title": "Database Optimization",
      "header":"Database search optimization",
      "description":"Used PeeWee Object Relational Mapping\n" +
      "                                and PostGres RDBMS to optimize large\n" +
      "                                search queries and prevent memory overflow errors\n" +
      "                                as part of a refactor for Brainspell.\n" +
      "                            </p>\n" +
      "                            <p><a href=\"https://github.com/OpenNeuroLab/brainspell-neo\">Code</a>"
  },
  {
    "title" : "Protein Domain Boundary Prediction",
      "header": "Parsing the UniProt Database to discover Homology Relations",
      "description":"Based on information contained in the BLAST database,\n" +
      "                                I designed a sequence weighting procedure to evaluate\n" +
      "                                boundary regions of transmembrane helices on specified\n" +
      "                                query proteins. I used evolutionary distance measures\n" +
      "                                coupled with phylogenetic tree construction to evaluate\n" +
      "                                the \"most similar\" proteins to the target and created\n" +
      "                                an annotation transfer protocol based on this similarity.\n" +
      "                                My weighted consensus TMH prediction tool POC was able\n" +
      "                                showed accuracies of up to 30% greater than\n" +
      "                                industry leading software programs.\n" +
      "                            </p>\n" +
      "                            <p><a href=\"https://github.com/Sharabesh/bioe144\">Code</a>"
  },
  {
    "title": "Protein Structure Prediction",
      "header":"Analyzing protein Multi-Domain Architectures through consensus",
      "description":"Designed software to correct existing errors in\n" +
      "                                UniProt Database based on metaserver consensus approaches.\n" +
      "                            </p>\n" +
      "                            <p><a href=\"https://github.com/Sharabesh/MDA\">Code</a>"
  },
  {
    "title": "iOS Development",
      "header":"Development of a iOS Calculator Application",
      "description":"Early experiments with iOS through the creation\n" +
      "                                of a Calculator application"

  }
];

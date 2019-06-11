const portfolio_data = [
  {
    title: 'Ethereum Decentralized Exchange',
    header: 'Designing a more efficient blockchain decentralized exchange',
    description: `
              Together with Dawn Song's Research team out of UC Berkeley, I worked towards designing a
              more rapid decentralized exchange. This project fundamentally relied
              on integrating state-channels to prevent frequent updates "on chain"
              
          `
  },
  {
    title: 'Platform Engineering With Raydiant Oxymetry',
    header: 'Raydiant Oximetry, Fetal Pulse Oximetry',
    description: `
          Beginning Fall 2016, I have been working with
          Raydiant Oximetry and the Citris Bantao Institute
          to develop a real-time fetal pulse
          monitoring system. Building off the communication
          protocols for our monitoring devices,
          I built a system to constantly read and process
          data using a proprietary signal processing algorithm.
      `
  },
  {
    title: 'NP-Complete Approximation',
    header:
      'Designing an NP-Complete Approximation Algorithm using Simulated Annealing',
    description: `
          We sought to solve a variant of a betweenness problem (a proven NP-Complete Problem)
          Basically, we were given a series of constraints of the form A B C
          (which indicates C cannot lie between A and B) and tried to find the optimal
          ordering such that no constraint was violated. Our approach used simulated annealing
          and made random swaps to try to improve a cost function defined by constraints violated.
          There are also quite a few performance enhancements including multithreading, etc.
          The complete code is <a href="https://github.com/Sharabesh/NP-Complete_Solution">here</a>
        `
  },
  {
    title: 'Python Recursive Art',
    header: 'Recursive Art Using the Python Turtle Module',
    description: `
        Using the Python Turtle Graphics Module to Design recursion based art.
        Designed for a competition out of UC Berkeley's CS61A course (2nd place).`
  },
  {
    title: 'Analytics Platform Development',
    header: 'Designing a system for analytics into team behavior',
    description: `
          As a subsidiary assignment while at Cisco Systems, I worked
          on designing a user-friendly tool to voice complaints and
          generate some quick analytics for internal use.
          This project won the local summer design competition.
          The code is all <a href="https://github.com/Sharabesh/InternCorner">Here</a>
          and you can actually visit the site (live on Heroku)
           <a href="https://internbridge.herokuapp.com">Website</a>

    `
  },
  {
    title: 'Alpha-beta pruning with game trees',
    header: 'Optimizing AI decision making',
    description: `
          As part of a java-based implementation
          of Ataxx (a board game similar to chess)
          I worked on developing an AI for players to
          compete against.
          To allow the AI to evaluate possibilities several moves in
          advance of the current position, I worked
          on integrating alpha-beta pruning on the generated game-trees to optimize
          AI response speed
      `
  },
  {
    title: 'Javascript Graphics',
    header:
      'Implementing JavaScript Graphics to show regions of Neural Activation',
    description: `
          Used machine-parsed neuroimaging activation
          data to map activation patterns onto 3D
          interactive coordinate system. Data is accumulated from hundreds of articles
          and thresholded to yield specific regions most often corresponding to
          the particular keyword query.
      `
  },
  {
    title: 'Database Optimization',
    header: 'Database search optimization',
    description: `
          Used PeeWee Object Relational Mapping
          and PostGres RDBMS to optimize large
          search queries and prevent memory overflow errors
          as part of a refactor for Brainspell.
          </p>
          <p><a href="https://github.com/OpenNeuroLab/brainspell-neo">Code</a>
    `
  },
  {
    title: 'Protein Domain Boundary Prediction',
    header: 'Parsing the UniProt Database to discover Homology Relations',
    description: `
          Based on information contained in the BLAST database,
          I designed a sequence weighting procedure to evaluate
          boundary regions of transmembrane helices on specified
          query proteins. I used evolutionary distance measures
          coupled with phylogenetic tree construction to evaluate
          the "most similar" proteins to the target and created
          an annotation transfer protocol based on this similarity.
          My weighted consensus TMH prediction tool POC was able
          showed accuracies of up to 30% greater than
          industry leading software programs.
          </p>
          <p><a href="https://github.com/Sharabesh/bioe144">Code</a>
    `
  },
  {
    title: 'Protein Structure Prediction',
    header: 'Analyzing protein Multi-Domain Architectures through consensus',
    description: `
          Designed software to correct existing errors in
          UniProt Database based on metaserver consensus approaches.
          </p>
          <p><a href="https://github.com/Sharabesh/MDA">Code</a>
        `
  },
  {
    title: 'Predictive Safety',
    header:
      'A Machine Learning backed safety analysis program for student safety',
    description: `
        Backed by a grant from the skydeck fund, I worked to develop a
        react-native application that used predictive machine learning techniques 
        to plot out and group individuals along optimal routes to mitigate their
        exposure to crime. 
    `
  }
];

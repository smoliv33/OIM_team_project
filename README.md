# OIM_team_project
team project
team members: Olivia San, Eric Truong

# “Text-to-Product: Turning digital ideas into physical products”

### The Big Idea: What is the main idea of your project? What topics will you explore and what will you accomplish? Describe your minimum viable product (MVP) and your stretch goal.

In an era where design and technologies have begun to intersect more than ever. This project aims to experiment with the limits of CAD(Computer-Aided Design). 
To do so, we intend to develop a tool that converts written descriptions into CAD models in Onshape. This research aims to experiment with understanding a new way to conceptualize and create through text.
To achieve success in this process, an integration of (NLP) Natural Language Processing and CAD technology through Onshape. 
This tool will aim to understand and interpret text inputs to convert them into Python code and then into a 3D model through Featurescript, Onshape's programming language. 
This approach will enable CAD to become more accessible and potentially improve design processes, allowing more time for individual users to refine concepts and ideas. 
MVP:
Our goal is to create an application capable of converting text instructions that can be turned into 3D CAD drawings. We aim to design a program to generate a cube that can provide instructions on its length, width, and height. By doing this, the MVP will serve as a proof of concept, showing that further research can be performed and presenting the idea's potential. 

Stretch Goal:
While being able to generate a cube would be great, pushing the concept to its limit would present even more potential applications. To achieve this, we aim to expand the capability of the tool to be able to then convert the 3D model in Onshape to a slicer such as Cura or Prusa slicer, using optimal infill, organic supports, as well as a randomized z-seam to be able to slice the file then accordingly. Afterward, the tool would then be able to export the resulting g-code to a 3D printer through octo-print wirelessly. This will enable an interactive and improved design experience as text can be turned into a physical idea with a click of two buttons. 


### Learning Objectives: Since this is a team project, you may want to articulate both shared and individual learning goals.

After careful consideration, we have decided to categorize our learning objectives into two categories: shared team learning objectives and individual learning objectives. By doing so, we aim to tailor our objectives to cover the goals of everyone in the group and what each individual specializes in, allowing for a cohesive advancement of the project. 
Shared Team Goals:
Understanding and Application of NLP: We as a group aim to, through this project, gain a comprehensive knowledge of how NLP can be used in interpreting text inputs for design and potential implementation in design as a whole.
Integration of NLP with CAD: We aim to develop the skillset required to integrate algorithms with Onshape and focus on converting text descriptions into Featurescript.
End-to-End Process Management: We intend to be able to become adept at comprehending the entire process flow, meaning understanding how the text input works, how it converts into the creation of a 3D model, the slicing of the STL file, and the preparation of the printer for 3D printing as we aim to provide a seamless transition between each of the stages. 
Collaborative Software Development: This project is an opportunity to attempt ideas like peer programming and allow us a platform to enhance our skills in joint development and project management. 
Problem-Solving and Innovation: We hope that the project helps nurture our ability to solve problems by utilizing new, innovative technologies, as this will be something that we will all likely encounter in our future careers. 
Specialization in NLP and Python Development: 
We aim to focus on understanding the utilization of NLP libraries and how to create scripting to convert text into CAD software. 
Understanding Development Workflow: 
Our goal is to be able to better understand the workflow of CAD model creation and how CAD works on a fundamental level in terms of the coding of CAD. I believe that learning this will enable me to better understand the concepts of designing 3D objects in a digital format, as it is something that I am not accustomed to. 

Individual Learning Goals
Olivia San: I hope to apply what I learned in this class to our real-life project. I want to deepen my knowledge in Python through practice and application to better understand the industry, incorporate technologies, and solve the problems facing us today. I also would like to better understand CAD and navigate its intersection with programming. 
Eric Truong: With the experience that I learned from this project, I hope that I will be able to use the knowledge that I gain from this to be able to implement in our real-world projects such as Etos, a research focused on customized furniture using Chinese joinery techniques as well as Theia, a company formed by me and two others focused on creating designer lamps using 3D printing. What I gain from this project will help me streamline my design's production and manufacturing processes and provide a real-world example of how I can use Python to solve problems that I may face in the future. 
Proficiency in CAD Modeling and Featurescript: 
I aim to develop my skills in understanding the conversion of the Python script into Featurescript and develop the skills to allow for a complete understanding of how CAD software functions as I can design models myself as well as understand the general idea of how CAD works, however, I have never delved deep into how I could potentially code the designing process. Doing this, I believe this would be invaluable to my learning as I will be able to potentially create scripts that could help streamline my designing process featurescript is not a language that I will likely learn but will be something that I will encounter on a daily basis. 

Advanced 3D Printing and Slicing Techniques: 
As a team member, I aim to be a specialist in 3D printing, which includes the understanding of advanced slicer settings such as optimal infill, g-code optimization, and CAD, and also be able to leverage my ability in shape to be able to understand how to design for 3D printing, knowing if a design is able to be printed or not. In addition, I will be learning how to use OctoPrint in order to enable wireless 3D printer 
communication with my code, as it will require a raspberry pi to function. 


### Implementation Plan: This part may be somewhat ambiguous initially. You might have identified a library or a framework that you believe would be helpful for your project at this early stage. If you're uncertain about executing your project plan, provide a rough plan describing how you'll investigate this information further.
Initial Tools and Technologies
Natural Language Processing (NLP): We plan to utilize Python-based NLP libraries such as NLTK (Natural Language Toolkit) in order to interpreting text inputs. In addition, we plan to use ChatGPT to be able to help with the interpretation. These libraries provide us the ability for parsing language as well as understanding text. 
CAD Software: We will be using Onshape for the CAD modeling due to its API, its Featurescript language, and it being on the cloud offers us the flexibility that we need in order to integrate with the NLP outputs. 
3D Printing Software: We are planning to use Prusa Slicer to be able to convert the CAD model into printer-ready files. We will also explore the utilization of OctoPrint to be able to print from the computer rather than with an SD Card.


### Project Schedule: You have 6 weeks (roughly) to finish the project. Draft a general timeline for your project. Depending on your project, you might be able to provide a detailed schedule or only an overview. Preparation of a longer project is also accompanied by present uncertainty, and this schedule will likely require revisions as the project progresses.
Initial Exploration (Weeks 1-2):
For the first two weeks, we aim to research existing research and products as well as tutorials on NLP and Onshape API capabilities. To do this, we intend to experiment with different libraries to understand how suitable they are for our project as well as what we potentially need to learn to ensure that our project works. 
Prototype Development (Weeks 3):
For weeks 3 and 4, we intend to develop the python script using the NLP library to be able to convert the text into basic CAD formats as well as use feature script to be able to interpret these results into 3D models. 
Integration and Refinement (Weeks 4-5):
For our final weeks, we intend to ensure that everything works according to our goals as we want a seamless interaction between the CAD and the NLP outputs. We also intend to streamline the process from being able to convert the CAD model into a sliced format and potentially see if it is possible to present our result with a printer in the classroom. 
Advanced Development and Stretch Goal (Weeks 6):
This last week will focus on the automation to the 3D printer using Octoprint as well as making sure that we are able to adapt to potential challenges as needed.


### Collaboration Plan: How will you collaborate with your teammates on this project? Will you divide tasks and then incorporate them separately? Will you undertake a comprehensive pair program? Explain how you'll ensure effective team collaboration. This may also entail information on any software development methodologies you anticipate using (e.g. agile development). Be sure to clarify why you've picked this specific organizational structure.
For the collaboration of this project, our team plans to divide tasks and incorporate them separately. In the meantime, we are also going to plan, research, execute our vision, and tackle roadblocks together. This would ensure effective team collaboration, as well as an overall holistic approach that enables both team members to contribute their ideas and skills to various parts, bounce ideas off of each other, and provide mutual feedback and insights. 

### Risks and Limitations: What do you believe is the most significant threat to this project's success? 
Backup Plans for Tool Incompatibility: In case certain NLP libraries or features in Onshape do not meet our needs, we will maintain a list of alternative tools to explore.
Regular Check-Ins with Advisors: To ensure we are on the right track and to seek guidance on overcoming technical hurdles.


### Additional Course Content: What topics do you believe will be beneficial to your project?
Natural Language Processing (NLP), and Integration of NLP with CAD
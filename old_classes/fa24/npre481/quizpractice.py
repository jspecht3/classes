questions = [
    "Which sentence would you accept as a reviewer or editor that best reflects what you learned in NPRE/GLBL 481?",
    "Which sentence would you accept as a reviewer or editor that best reflects what you learned in NPRE/GLBL 481?",
    "What are some of the duties and expectations of editorial-board members?",
    "What is the mode of 1, 3, 6, 6, 6, 6, 7, 7, 12, 12, 17?",
    "What is a normal distribution of observations? Draw a figure. Include the population mean.",
    "How may editorial-board members identify and select potential reviewers for manuscripts?",
    "According to Grant Man, what is the key to talking to faculty about a possible undergrad proposal?",
    "If a correlation coefficient (r2) is equal to 0.81, what does this mean in terms of the validity of the regression?",
    "Your manuscript has been reviewed and you have many review comments. What should you do to advance to the next stage in publication?",
    "You have agreed to be an anonymous reviewer for a manuscript that has been submitted for publication. What options to you have as a reviewer?",
    "What is a galley proof?",
    "What is a control in a manuscript?",
    "Although it may seem immodest, why can it be helpful to explicitly indicate what is a new contribution to a research area in a manuscript?",
    "What question(s) are we trying to answer when writing a Project Feasibility Report?",
    "According to Grant Man, what are the three major arguments in creating an undergrad research proposal?",
    "List three disadvantages of using copy/paste to acquire figures for a manuscript?",
    "True or false? (Circle one). Champaign has an active municipal landfill located north of the city.",
    "What is the easiest way to write a book review?",
    "What does oil shale in the Green River Formation in the U.S. contain that could be a valuable commodity some day?",
    "Which sentence would you accept as a reviewer or editor that best reflects what you learned in NPRE/GLBL 481?",
    "Which sentence would you accept as a reviewer or editor that best reflects what you learned in NPRE/GLBL 481?",
    "What grade do you expect for NPRE/GLBL 481?",
]

choices = [
    "(a) The valve needs to be turned fully clockwise.\n(b) All of the switches on the instrument console were flashing off and on.\n(c) The control rods see the lower part of the reactor vessel.\n(d) The timer on the filter press said that it was time to turn off the power.",
    "(a) A cylinder that contained an unknown solid material and a gray liquid at the bottom was opened.\n(b) Each participant who remained near the entrance of the classroom and seemed interested was interviewed.\n(c) The students cleaned the optical system three days ago with a cleaning fluid.\n(d) Three abandoned crates one labeled with DU and the other two labeled as NASA were forced open.",
    "(a) They are compensated for their time with a modest economic incentive.\n(b) They review draft and revised manuscripts.\n(c) They re-write draft manuscripts to accelerate the review-publication process.\n(d) They have the option of communicating directly with authors if needed.",
    "(a) 1\n(b) 6\n(c) 7\n(d) 12",
    "(a) Bell curve with mean at the peak.",
    "(a) Contact recent authors cited in the reference section of the manuscript.\n(b) Referrals, suggestions, and recommendations provided by people who do not agree to review the manuscript.\n(c) Known experts about the topic.\n(d) All of the above.",
    "(a) Create ans submit a pre-proposal.",
    "(a) 81 percent of the data could be explained while 19 percent could not by linear regression.",
    "(a) Accept or reject the comments, revise the manuscript, resubmit and assume that the Editor will accept the manuscript for publication.\n(b) Accept every suggestion, revise the manuscript, resubmit and assume that the Editor will accept the manuscript for publication.\n(c) When in doubt, contact the reviewers to seek clarification about the review comments, then revise the manuscript, resubmit and assume that the Editor will accept the manuscript for publication.\n(d) Make a detailed list of how you responded to each review comment, revise the manuscript, then resubmit it to the Editor.",
    "(a) Ignore the Methods and Materials section. The content of this section will be reviewed by the Technical Editor.\n(b) You can go beyond editing and rewrite the text as needed.\n(c) Check the references when encountered in the text. Are they present or missing in references cited section?\n(d) Read the entire manuscript first, make a list of questions, then contact the authors to ask your questions.",
    "(a) It is the name of the manuscript when first submitted to the Editor for publication.\n(b) It is the file that contains all the figures and photographs to be inserted into the text.\n(c) A published addendum of corrections to errors in a published paper (something to avoid).\n(d) A mock-up of the accepted manuscript for the final author-level review.",
    "(a) Statistical replication of measured data.\n(b) The place of employment of the authors, or the source of funding of a sponsored project.\n(c) The presence of all parts of a manuscript (abstract, introduction, etc.)\n(d) A basis for comparisons.",
    "(a) Some reviewers may simply not recognize a new discovery or idea.\n(b) Some reviewers may not be able to fully appreciate the potential impact that the manuscript could have once it is published.\n(c) It can help convince the Editor that the manuscript should be published despite other issues.\n(d) All of above.",
    "(a) Will more jobs be created for the general public?\n(b) Will historical buildings be negatively impacted?\n(c) Should we take the proposed idea to the next level of planning?\n(d) All of the above.",
    "(a) Is this needed? What is the plan? Are you qualified?",
    "(a) It could violate copyright laws, it could hurt your manuscript’s credibility, and you might not find the right figures that you need.",
    "(a) True\n(b) False",
    "(a) What is contained within the book, your opinion on it, did it have a good writing style, was it free from grammatical errors, do the graphs and tables make sense, would you recommend it to someone?",
    "(a) oil\n(b) kerogen\n(c) uranium\n(d) kaolin",
    "(a) The groundwater near the decommissioned power plant got contaminated with chlorinated hydrocarbons (CH). CH can be resistant to biodegradation.\n(b) The groundwater near the decommissioned power plant was contaminated with chlorinated hydrocarbons. CH can be resistant to degradation.\n(c) The groundwater near the decommissioned power plant got contaminated with chlorinated hydrocarbons (CH) which can be resistant to degradation.\n(d) The groundwater near the decommissioned power plant was contaminated with chlorinated hydrocarbons. Chlorinated hydrocarbons can be resistant to biodegradation.",
    "(a) Because of climate change, new coal-fired power plants are not being built in Poland-- a potentially new nuclear county within the European Union.\n(b) Due to climate change, new coal fired power plants are not being built in Poland, a potentially new country, within the european union.\n(c) Because of climate change, new coal fired power plants, aren't being built in Poland, a potentially new nuclear county, within the European union.\n(d) Due to climate change, new coal-fired power plants aren't being built in Poland, a potentially new nuclear county, within the european union.",
    "(a) A\n(b) B\n(c) C\n(d) D"
    ]

answers = [
    "b",
    "c",
    "b",
    "b",
    "a",
    "d",
    "a",
    "a",
    "d",
    "c",
    "a",
    "d",
    "d",
    "c",
    "a",
    "a",
    "b",
    "a",
    "b",
    "d",
    "a",
    "a",
]

def quiz():
    score = 0
    length = 0
    for question, choice, answer in zip(questions, choices, answers):
        print(question)
        user_answer = input(choice).lower()
        if user_answer in answer:
            print('Correct!!!')
            score += 1
        else:
            print('Incorrect, the right answer is:', answer)
        length += 1
        print("You have gotten " + str(score) + '/' + str(length) + " correct. That is " + str((score/length)*100) + " percent.")
    
quiz()
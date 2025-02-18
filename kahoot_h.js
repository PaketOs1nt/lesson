var questions = [];
var info = {
    numQuestions: 0,
    questionNum: -1,
    lastAnsweredQuestion: -1,
    defaultIL:true,
    ILSetQuestion:-1,
};

function FindByAttributeValue(attribute, value, element_type)    {
element_type = element_type || "*";
var All = document.getElementsByTagName(element_type);
for (var i = 0; i < All.length; i++)       {
    if (All[i].getAttribute(attribute) == value) { return All[i]; }
}
}

function parseQuestions(questionsJson){
    let questions = []
    questionsJson.forEach(function (question){
    let q = {type:question.type, time:question.time}
    if (['quiz', 'multiple_select_quiz'].includes(question.type)){
        var i=0
        q.answers = []
        q.incorrectAnswers = []
        question.choices.forEach(function(choise){
            if (choise.correct) {
                q.answers.push(i)
            }
            else{
                q.incorrectAnswers.push(i)
            }
            i++
        })
    }
    if (question.type == 'open_ended')
    {
        q.answers = []
        question.choices.forEach(function(choise){
            q.answers.push(choise.answer)
        })
    }
    questions.push(q)
})
    return questions
}

function hack(token){
    const url = 'https://kahoot.it/rest/kahoots/' + token;
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('');
            }
            return response.json();
        })
        .then(data => {
            questions=parseQuestions(data.questions)
            info.numQuestions=questions.length
        })
        .catch(error => {
            info.numQuestions = 0
        });
    }

function onQuestionStart(){
    var question = questions[info.questionNum]
    highlightAnswers(question)

}

function highlightAnswers(question){
    question.answers.forEach(function (answer) {
        setTimeout(function() {
            FindByAttributeValue("data-functional-selector", 'answer-'+answer, "button").style.boxShadow = 'none';
        }, 0)
    })
}

document.addEventListener('keydown', (event)=> {
    if (event.key == "h")
    {
        var textElement = FindByAttributeValue("data-functional-selector", "question-index-counter", "div")
        if (textElement){
            info.questionNum = +textElement.textContent - 1
        }
        if (FindByAttributeValue("data-functional-selector", 'answer-0', "button") && info.lastAnsweredQuestion != info.questionNum) 
        {
            info.lastAnsweredQuestion = info.questionNum;
            onQuestionStart()
        }
    }
})

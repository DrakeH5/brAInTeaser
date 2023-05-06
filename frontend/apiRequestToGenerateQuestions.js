const apiRequestToGenerateQuestions = async(input) => {
    var questions;
    await fetch("http://localhost:5000/generateQuestions", {
        method: 'POST', 
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            input: input
        })
    })
        .then((response) => response.json())
            .then((json) => {
                console.log(json)
                questions = json;
            });
    return questions;
}
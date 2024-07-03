(function (){
    const optionSelect = document.querySelector("select");
    const invisibleInput = document.querySelector(".invisible-input");
    if (invisibleInput && optionSelect) {
        optionSelect.addEventListener("change", function (evt) {
            invisibleInput.setAttribute("value", optionSelect.value);
            console.log(invisibleInput.value);
        })
    }
    const lifeInput = document.querySelector("#life");
    if (lifeInput){
        lifeInput.addEventListener("input", function(evt) {
            console.log(lifeInput.value)
            lifeInput.setAttribute("value", lifeInput.value);
        });
    }

    const backLifeButton = document.querySelector(".back-life-button")
    if (backLifeButton) {
        backLifeButton.addEventListener("click", function (evt){
            evt.preventDefault()
            const lifeInput = document.querySelector("#life");
            lifeInput.setAttribute("value", (Number.parseInt(lifeInput.value) - 1).toString())
        })
    }

    const frontLifeButton = document.querySelector(".front-life-button")
    if (frontLifeButton) {
        frontLifeButton.addEventListener("click", function (evt){
            evt.preventDefault()
            const lifeInput = document.querySelector("#life");
            lifeInput.setAttribute("value", (Number.parseInt(lifeInput.value) + 1).toString())
        })
    }
})();
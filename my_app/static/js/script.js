(function (){
    const uploadLifeBar = (lifeInput, damageBar) => {
            lifeInput.setAttribute("value", lifeInput.value);
            damageBar.style.left = (((lifeInput.value * 100) / lifeInput.max)).toString() + '%'
    }

    const optionSelect = document.querySelector("select");
    const invisibleInput = document.querySelector(".invisible-input");
    if (invisibleInput && optionSelect) {
        optionSelect.addEventListener("change", function (evt) {
            invisibleInput.setAttribute("value", optionSelect.value);
            console.log(invisibleInput.value);
        })
    }
    const lifeInput = document.querySelector("#life");
    const damageBar = document.querySelector(".damage-bar")
    if (lifeInput){
        lifeInput.addEventListener("input", function (evt){
            uploadLifeBar(lifeInput, damageBar);
        });
    }

    const backLifeButton = document.querySelector(".back-life-button")
    if (backLifeButton) {
        backLifeButton.addEventListener("click", function (evt){
            evt.preventDefault()
            const lifeInput = document.querySelector("#life");
            lifeInput.value = (Number.parseInt(lifeInput.value) - 1).toString();
            uploadLifeBar(lifeInput, damageBar)
        })
    }

    const frontLifeButton = document.querySelector(".front-life-button")
    if (frontLifeButton) {
        frontLifeButton.addEventListener("click", function (evt){
            evt.preventDefault()
            const lifeInput = document.querySelector("#life");
            lifeInput.value = (Number.parseInt(lifeInput.value) + 1).toString();
            uploadLifeBar(lifeInput, damageBar)
        })
    }


})();
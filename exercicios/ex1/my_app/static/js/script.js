(function () {
    const copyButton = document.querySelector("#copy-button");
    copyButton.addEventListener("click", function (event){
        const codText = document.querySelector("#cod-text").textContent.split((": "))[1].trim();

        copyButton.style.backgroundImage = "url('/static/img/check-icon.png')";
        copyButton.style.width = "20px";

        navigator.clipboard.writeText(codText);
    })
})();
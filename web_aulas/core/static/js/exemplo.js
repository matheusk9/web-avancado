function altera_texto() {
    const myButton = document.getElementById('myButton');
    const myText = document.getElementById('myText');

    myButton.addEventListener('click', function() {
        myText.textContent = 'Texto alterado!';
    });
}
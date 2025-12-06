const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

// Funcionalidade de item ativo no menu lateral
allSideMenu.forEach(item => {
    const li = item.parentElement;

    item.addEventListener('click', function () {
        allSideMenu.forEach(i => {
            i.parentElement.classList.remove('active');
        })
        li.classList.add('active');
    })
});


// TOGGLE SIDEBAR
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

// Alternar a classe 'hide' no sidebar ao clicar no menu
menuBar.addEventListener('click', function () {
    sidebar.classList.toggle('hide');
})


// Manter o sidebar escondido em telas pequenas
if (window.innerWidth < 768) {
    sidebar.classList.add('hide');
}

// Listener para redimensionamento de janela
window.addEventListener('resize', function () {
    if (this.innerWidth < 768) {
        sidebar.classList.add('hide');
    }
})


document.getElementById('add-question-btn').addEventListener('click', function () {
    var container = document.getElementById('dynamic-inputs-container');

    // O HTML dos novos inputs, usando title[] e question[]
    var newInputsHTML = `
            <div class="dynamic-input-group" style="margin-top: 15px; padding-top: 15px; border-top: 1px dashed #33425A;">
                <input type="text" name="title[]" placeholder="Inclua o título da pergunta (Adicional)" class="input-group" required/> 
                <input type="text" name="question[]" placeholder="Inclua as opções de respostas (Adicional)" class="input-group" required/>
            </div>
        `;

    // Insere os novos inputs dentro do contêiner dinâmico
    container.insertAdjacentHTML('beforeend', newInputsHTML);
});
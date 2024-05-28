document.addEventListener("DOMContentLoaded", function() {
    // Função para fazer a solicitação AJAX
    function fetchIndicators() {
        // Faz uma solicitação AJAX para o servidor Node.js
        fetch('http://localhost:8097/indicadores')
            .then(response => response.json())
            .then(data => {
                // Atualiza os indicadores com os dados recebidos
                data.forEach((indicador, index) => {
                // Atualiza os indicadores com os dados recebidos
                    document.getElementById(`value${index + 1}`).textContent = indicador.value;
                    document.getElementById(`goal${index + 1}`).textContent = `Meta: ${indicador.goal}`;
                    document.getElementById(`percentage${index + 1}`).textContent = `${(indicador.value / indicador.goal * 100).toFixed(2)}%`;
                })
            })
            .catch(error => console.error('Erro ao buscar dados:', error));
    }
    fetchIndicators();
});
document.addEventListener("DOMContentLoaded", function() {
    // Função para fazer a solicitação AJAX
    function fetchIndicators() {
        // Faz uma solicitação AJAX para o servidor Node.js
        fetch('http:/localhost:3306/sensores')
            .then(response => response.json())
            .then(data => {
                // Atualiza os indicadores com os dados recebidos
                data.forEach((sensores, index) => {
                    document.getElementById(`value${index + 1}`).textContent = sensores.value;
                    document.getElementById(`goal${index + 1}`).textContent = `Meta: ${sensores.goal}`;
                    document.getElementById(`percentage${index + 1}`).textContent = `${(sensores.value / sensores.goal * 100).toFixed(2)}%`;
                });
            })
            .catch(error => console.error('Erro ao buscar dados:', error));
    }

    fetchIndicators();

    var ctx1 = document.getElementById('acuraciaChart').getContext('2d');
    var ctx2 = document.getElementById('perdaChart').getContext('2d');

    var acuraciaChart = new Chart(ctx1, {
        type: 'line',
        data: {
            labels: Array.from({length: 301}, (_, i) => i),
            datasets: [
                {
                    label: 'Acurácia de Treino',
                    data: [/* Colocar aqui os dados de acurácia de treino */],
                    borderColor: 'blue',
                    fill: false,
                },
                {
                    label: 'Acurácia de Teste',
                    data: [/* Colocar aqui os dados de acurácia de teste */],
                    borderColor: 'orange',
                    fill: false,
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            title: {
                display: true,
                text: 'Acurácia de Treino e Teste'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Épocas'
                    },
                    ticks: {
                        stepSize: 50
                    }
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Acurácia'
                    },
                    ticks: {
                        min: 0.50,
                        max: 0.70,
                        stepSize: 0.05,
                        callback: function(value) {
                            return value.toFixed(2);
                        }
                    }
                }
            }
        }
    });

    var perdaChart = new Chart(ctx2, {
        type: 'line',
        data: {
            labels: Array.from({length: 301}, (_, i) => i),
            datasets: [
                {
                    label: 'Perda de Treino',
                    data: [/* Colocar aqui os dados de perda de treino */],
                    borderColor: 'green',
                    fill: false,
                },
                {
                    label: 'Perda de Teste',
                    data: [/* Colocar aqui os dados de perda de teste */],
                    borderColor: 'red',
                    fill: false,
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            title: {
                display: true,
                text: 'Perda de Treino e Teste'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Épocas'
                    },
                    ticks: {
                        stepSize: 50
                    }
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Perda'
                    },
                    ticks: {
                        min: 0.25,
                        max: 0.60,
                        stepSize: 0.05,
                        callback: function(value) {
                            return value.toFixed(2);
                        }
                    }
                }
            }
        }
    });
});

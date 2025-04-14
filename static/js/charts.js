function createCategoryChart(categories, amounts) {
    // Gets canvas element by ID, similar to Python accessing GUI elements.
    var ctx = document.getElementById('categoryChart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'bar',  // Bar chart, like Matplotlib's plt.bar().
        data: {
            labels: categories,  // Array for x-axis, like a Python list.
            datasets: [{
                label: 'Expenses by Category',
                data: amounts,  // Array for y-axis values.
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function (value) {
                            return '$' + value.toLocaleString();
                        }
                    }
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: (context) => `$${context.parsed.y.toLocaleString()} in ${context.label}`
                    }
                }
            }
        }
    });
}

function createRunningTotalChart(dates, running_totals) {
    // Access canvas for line chart rendering.
    var ctx = document.getElementById('runningTotalChart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'line',  // Line chart, like Matplotlib's plt.plot().
        data: {
            labels: dates,
            datasets: [{
                label: 'Running Total',
                data: running_totals,
                fill: false,
                borderColor: 'rgba(153, 102, 255, 1)',
                tension: 0.1  // Smooths the line.
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function (value) {
                            return '$' + value.toLocaleString();
                        }
                    }
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: (context) => `$${context.parsed.y.toLocaleString()} on ${context.label}`
                    }
                }
            }
        }
    });
}


// initlialise charts after page load
function initCharts() {
    console.log("initialising charts...")
    console.log("window.chartData:", window.chartData);
    if (window.chartData) {
        console.log("Rendering category chart with:", window.chartData.categories, window.chartData.amounts);
        createCategoryChart(window.chartData.categories, window.chartData.amounts);
        console.log("Rendering total chart with:", window.chartData.dates, window.chartData.running_totals);
        createRunningTotalChart(window.chartData.dates, window.chartData.running_totals);
    } else {
        console.error("Chart data not found!");
    }
}

// Run initialisation when DOM is fully loaded
document.addEventListener('DOMContentLoaded', initCharts);
// Load Google Charts
google.charts.load('current', {'packages':['corechart', 'bar']});
google.charts.setOnLoadCallback(initCharts);

// Chart instances
let charts = {};

function initCharts() {
    const chartIds = ['intensity_chart', 'likelihood_chart', 'relevance_chart', 'year_chart', 'country_chart', 'region_chart'];

    chartIds.forEach(id => {
        const chartDiv = document.getElementById(id);
        if (chartDiv) {
            const chart = createChart(id);
            charts[id] = chart;
        }
    });

    // Initially fetch data and draw charts
    fetchDataAndDrawCharts();
}

function createChart(elementId) {
    const chartOptions = {
        PieChart: { title: 'Data', pieHole: 0.4, animation: { startup: true, duration: 1000, easing: 'out' } },
        BarChart: { title: 'Data', hAxis: { title: 'Category' }, vAxis: { title: 'Value' }, legend: { position: 'none' }, animation: { startup: true, duration: 1000, easing: 'out' } },
        LineChart: { title: 'Data', hAxis: { title: 'Category' }, vAxis: { title: 'Value' }, legend: { position: 'none' }, animation: { startup: true, duration: 1000, easing: 'out' } },
    };

    switch (elementId) {
        case 'intensity_chart':
        case 'country_chart':
            return new google.visualization.PieChart(document.getElementById(elementId));
        case 'likelihood_chart':
        case 'year_chart':
        case 'region_chart':
            return new google.visualization.BarChart(document.getElementById(elementId));
        case 'relevance_chart':
            return new google.visualization.LineChart(document.getElementById(elementId));
        default:
            return null;
    }
}

function fetchDataAndDrawCharts() {
    // const endYear = document.getElementById('end_year').value || '';
    const endYear = document.getElementById('end_year').value || '2018';
    const topic = document.getElementById('topic').value || '';
    const sector = document.getElementById('sector').value || '';
    const region = document.getElementById('region').value || '';
    const country = document.getElementById('country').value || '';

    fetch(`/fetch_data?end_year=${endYear}&topic=${topic}&sector=${sector}&region=${region}&country=${country}`)
        .then(response => response.json())
        .then(data => {
            if (data.intensity_data) {
                drawChart('intensity_chart', data.intensity_data);
            }
            if (data.likelihood_data) {
                drawChart('likelihood_chart', data.likelihood_data);
            }
            if (data.relevance_data) {
                drawChart('relevance_chart', data.relevance_data);
            }
            if (data.year_data) {
                drawChart('year_chart', data.year_data);
            }
            if (data.country_data) {
                drawChart('country_chart', data.country_data);
            }
            if (data.region_data) {
                drawChart('region_chart', data.region_data);
            }
        })
        .catch(error => console.error('Error fetching data:', error));
}

function drawChart(elementId, data) {
    const chart = charts[elementId];
    if (!chart) return;

    const chartData = new google.visualization.DataTable();
    chartData.addColumn('string', 'Category');
    chartData.addColumn('number', 'Value');
    data.forEach(item => chartData.addRow([item.category, item.value]));

    const chartOptions = createChartOptions(elementId);
    chart.draw(chartData, chartOptions);
}

function createChartOptions(elementId) {
    switch (elementId) {
        case 'intensity_chart':
        case 'country_chart':
            return { title: 'Data', pieHole: 0.4, animation: { startup: true, duration: 1000, easing: 'out' } };
        case 'likelihood_chart':
        case 'year_chart':
        case 'region_chart':
            return { title: 'Data', hAxis: { title: 'Category' }, vAxis: { title: 'Value' }, legend: { position: 'none' }, animation: { startup: true, duration: 1000, easing: 'out' } };
        case 'relevance_chart':
            return { title: 'Data', hAxis: { title: 'Category' }, vAxis: { title: 'Value' }, legend: { position: 'none' }, animation: { startup: true, duration: 1000, easing: 'out' } };
        default:
            return {};
    }
}

function updateCharts() {
    const endYear = document.getElementById('end_year').value || '';
    const topic = document.getElementById('topic').value || '';
    const sector = document.getElementById('sector').value || '';
    const region = document.getElementById('region').value || '';
    const country = document.getElementById('country').value || '';

    fetch(`/fetch_data?end_year=${endYear}&topic=${topic}&sector=${sector}&region=${region}&country=${country}`)
        .then(response => response.json())
        .then(data => {
            if (data.intensity_data) {
                drawChart('intensity_chart', data.intensity_data);
            }
            if (data.likelihood_data) {
                drawChart('likelihood_chart', data.likelihood_data);
            }
            if (data.relevance_data) {
                drawChart('relevance_chart', data.relevance_data);
            }
            if (data.year_data) {
                drawChart('year_chart', data.year_data);
            }
            if (data.country_data) {
                drawChart('country_chart', data.country_data);
            }
            if (data.region_data) {
                drawChart('region_chart', data.region_data);
            }
        })
        .catch(error => console.error('Error fetching data:', error));
}

// Event listener for filter form
document.getElementById('filter-form').addEventListener('change', fetchDataAndDrawCharts);

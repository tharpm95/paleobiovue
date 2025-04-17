<template>
  <div>
    <h1>Data from API - Histogram Timeline</h1>
    <LineChart :chartData="chartData" :chartOptions="chartOptions" />
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import axios from 'axios';
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement);

export default defineComponent({
  components: {
    LineChart: defineComponent({
      name: 'LineChart',
      extends: Line,
      props: {
        chartData: {
          type: Object,
          required: true
        },
        chartOptions: {
          type: Object,
          default: () => ({
            responsive: true,
            plugins: {
              legend: {
                display: false
              }
            },
            scales: {
              x: {
                title: {
                  display: true,
                  text: 'Year'
                }
              },
              y: {
                title: {
                  display: true,
                  text: 'Values'
                }
              }
            }
          })
        }
      },
      mounted() {
        console.log('LineChart component mounted');
      },
      methods: {
        renderChart() {
          this.renderChart(this.chartData, this.chartOptions);
          console.log('Render chart called with data', this.chartData);
        }
      },
      watch: {
        chartData: {
          deep: true,
          handler(newValue, oldValue) {
            console.log('chartData changed:', oldValue, '->', newValue);
            if (this.$data._chart) {
              console.log('Chart data updated, re-rendering chart');
              this.renderChart();
            }
          }
        }
      }
    })
  },
  data() {
    return {
      chartData: {
        labels: [],
        datasets: [{
          label: 'Data Values',
          backgroundColor: '#42A5F5',
          data: []
        }]
      },
      chartOptions: {}
    };
  },
  created() {
    console.log('TimelineDisplay component created');
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios.get(process.env.VUE_APP_API_URL + '/data')
        .then(response => {
          console.log('API response received:', response.data);
          const items = response.data;
          this.chartData.labels = Object.keys(items);
          this.chartData.datasets[0].data = Object.values(items);
          console.log('Chart data updated with API data:', this.chartData);
        })
        .catch(error => {
          console.error('There was an error fetching the data:', error);
        });
    }
  }
});
</script>
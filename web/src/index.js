import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import {
  Chart,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  TimeScale,
  BarElement
} from 'chart.js';
import zoomPlugin from 'chartjs-plugin-zoom';

import 'bootstrap/dist/css/bootstrap.min.css';
import moment from 'moment';
// import 'mdb-ui-kit/css/mdb.min.css';

Chart.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  TimeScale,
  zoomPlugin
);

moment.locale("ru")
moment.updateLocale("ru-RU")

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

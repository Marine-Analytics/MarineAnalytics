import { Col, Card } from "react-bootstrap"
import { Line } from "react-chartjs-2"
import "chartjs-adapter-moment";

const format_time = (s) => new Date(s * 1e3);

export default function MetricsCard(props) {
    const state = props.state;
    const history = props.state.history;

    const stateExists = history.length !== 0;
    const predictExists = props.predict !== null;

    const stateAvailable = state.normalValues.min !== null || state.normalValues.max !== null;

    const stateLow = stateExists && state.normalValues.min !== null && history[history.length - 1].value < state.normalValues.min;
    const stateHigh = stateExists && state.normalValues.max !== null && history[history.length - 1].value > state.normalValues.max;

    const predictLow = predictExists && props.predict < state.normalValues.min;
    const predictHigh = predictExists && props.predict > state.normalValues.max;

    console.log(props.state);

    return <Col xxl="6" lg="6" md="6" sm="12" key={props.key}>
        <Card className="shadow h-100">
            <Card.Header>{props.title}</Card.Header>
            <Card.Body className="align-items-center">
                <Line
                    options={{
                        scales: {
                            y: {
                                beginAtZero: false
                            },
                            x: {
                                type: "time",
                                ticks: {
                                    autoSkip: true,
                                    maxTicksLimit: 15,
                                }
                            }
                        },
                        responsive: true,
                        locale: "ru-RU",
                        plugins: {
                            zoom: {
                                zoom: {
                                    wheel: {
                                        enabled: true,
                                    },
                                    pinch: {
                                        enabled: true
                                    },
                                    mode: 'xy',
                                },
                                pan: {
                                    enabled: true,
                                    mode: "xy",

                                },
                                limits: {
                                    // x: {
                                    //     min: props.state.history[0].date * 1e3,
                                    //     max: props.state.history[props.state.history.length - 1].date * 1e3,
                                    // }
                                }
                            },
                            legend: {
                                display: false,
                            },
                        }
                    }}
                    data={{
                        labels: props.state.history.map((e) => format_time(e.date)),
                        datasets: [{
                            data: props.state.history.map((e) => e.value),
                            tension: 0.25,
                            borderColor: '#0d6efd',
                            backgroundColor: '#1e7ffe'
                        }],
                    }}>
                </Line>

                <div class="mt-2">{(stateExists && stateAvailable) && <StateCard state={stateLow ? "low" : stateHigh ? "high" : "ok"} />}</div>

                {(predictExists) && <PredictCard state={predictLow ? "low" : predictHigh ? "high" : "ok"} value={props.predict} />}

            </Card.Body>
        </Card >
    </Col >
}

function StateCard(props) {
    return <div>
        <p className="card-title m-0 align-middle">
            <strong>Текущее состояние: </strong>
            {props.state === 'high'
                ? 'Аварийно высокое'
                : props.state === 'low'
                    ? 'Аварийно низкое'
                    : 'Норма'}
        </p>
    </div>
}

function PredictCard(props) {
    return <div>
        <p className="card-title m-0 align-middle">
            <strong>Прогноз: </strong>
            {String(props.value.toFixed(1)) + " " + (props.state === 'high'
                ? '(аварийно высокое)'
                : props.state === 'low'
                    ? '(аварийно низкое)'
                    : '(норма)')}
        </p>
    </div>
}
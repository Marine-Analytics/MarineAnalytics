import { Col, Card } from "react-bootstrap"
import { Bar } from "react-chartjs-2"
import "chartjs-adapter-moment";

function createDiagonalPattern(color = 'black') {
    let myCanvas = document.createElement('canvas');
    let drawingContext = myCanvas.getContext("2d");

    let color1 = "#CCCCCC", color2 = "#909090";
    let numberOfStripes = 40;
    for (let i = 0; i < numberOfStripes * 2; i++) {
        let thickness = 300 / numberOfStripes;
        drawingContext.beginPath();
        drawingContext.strokeStyle = i % 2 ? color1 : color2;
        drawingContext.lineWidth = thickness;
        drawingContext.lineCap = 'round';

        drawingContext.moveTo(i * thickness + thickness / 2 - 300, 0);
        drawingContext.lineTo(0 + i * thickness + thickness / 2, 300);
        drawingContext.stroke();
    }

    return drawingContext.createPattern(myCanvas, 'repeat')
}

export default function TOCard(props) {
    return <Col xxl="6" lg="6" md="6" sm="12">
        <Card className="shadow h-100">
            <Card.Header>Техническое обслуживание</Card.Header>
            <Card.Body className="align-items-center">
                <Bar
                    options={{
                        scales: {
                            y: {
                                beginAtZero: false,
                                stacked: true
                            },
                            x: {
                                stacked: true,
                            }
                        },
                        responsive: true,
                        locale: "ru-RU",
                        plugins: {
                            legend: {
                                display: false,
                            },
                        }
                    }}
                    data={{
                        labels: ["ТО №1", "ТО №1", "ТО №3", "ТО №4", "ТО №5 (прогноз)"],
                        datasets: [{
                            data: [62, 78, 71, 82, 0],
                            borderColor: '#0d6efd',
                            backgroundColor: '#1e7ffe'
                        },
                        {
                            data: [0, 0, 0, 0, 74],
                            borderColor: '#0d6efd',
                            backgroundColor: '#909090',
                        }],
                    }}>
                </Bar>
            </Card.Body>
        </Card >
    </Col >
}
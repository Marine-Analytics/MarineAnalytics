import { fetchVesselData } from '../DashboardApi';
import MetricsCard from "../components/MetricsCard";
import { Row } from "react-bootstrap"
import TOCard from './TOCard';
import { useEffect, useState } from 'react';


export default function StatsSection(props) {
    const [res, setRes] = useState(null);

    useEffect(() => {
        fetchVesselData(props.id).then((v) => setRes(v));
        const interval = setInterval(() => {
            console.log("aboba");
            fetchVesselData(props.id).then((v) => setRes(v));
        }, 15000);

        return () => clearInterval(interval);
    }, [props.id]);


    return res !== null
        ? <Row className="mt-1 gy-4 justify-content-center" key={props.id}>
            {res.sensors.map((e, i) =>
                <MetricsCard
                    title={e.name}
                    predict={e.predict}
                    id={i}
                    state={{
                        normalValues: {
                            min: e.normal.min,
                            max: e.normal.max,
                        },
                        history: e.history
                    }}
                    key={String(i) + String(props.id)}
                />
            )}
            <TOCard />
        </Row >
        : <p>Загрузка...</p>
}
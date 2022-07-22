import { Container } from "react-bootstrap"
import { useNavigate, useParams } from "react-router-dom";
import StatsSection from "./components/StatsSection";
import VesselPicker from "./components/VesselPicker";

export default function DashboardPage() {
    const navigate = useNavigate();
    const params = useParams();

    const vesselId = Number(params.vesselId) || null;

    return <Container fluid className="p-sm-5 pt-4">
        <VesselPicker
            selected={vesselId}
            vessels={[
                // TODO: fetch from api
                { id: 1, name: "Тестовый стенд" },
                { id: 2, name: "Судно" }
            ]}
            onSelect={(id) => { navigate(`/dashboard/${id}`) }}
        />
        {vesselId && <StatsSection id={vesselId} />}
    </Container >
}
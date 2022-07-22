import { MapContainer, TileLayer, Marker, Tooltip } from "react-leaflet"
import { useNavigate } from "react-router-dom";

const vessels = [
    { id: 1, name: "Тестовый стенд", position: [43.400545, 39.963706] },
    { id: 2, name: "Судно", position: [64.636800, 40.518800] }
]

export default function MapPage(props) {
    const navigate = useNavigate();

    return <div className="vh-100">
        <MapContainer attributionControl={false} center={[59.360156, 84.071523]} zoom={4} scrollWheelZoom={true} className="h-100">
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
            {vessels.map((e) => {
                return <Marker
                    riseOnHover={true}
                    key={e.id}
                    position={e.position}
                    eventHandlers={{
                        click: (_) => { navigate(`/dashboard/${e.id}`); }
                    }}
                >
                    <Tooltip key={e.id}>{e.name}</Tooltip>
                </Marker>
            })}
        </MapContainer>
    </div>
}
import { Dropdown } from "react-bootstrap";

export default function VesselPicker(props) {
    return <Dropdown onSelect={props.onSelect}>
        <Dropdown.Toggle className="m-0 p-0" style={{ boxShadow: "none" }} variant="transparent" id="dropdown-basic" size="lg">
            <span className="h3 mb-0 me-1">{props.selected !== null ? props.vessels.find(e => e.id === props.selected).name : "Не выбрано"}</span>
        </Dropdown.Toggle>

        <Dropdown.Menu>
            {props.vessels.map((e) =>
                <Dropdown.Item eventKey={e.id} active={e.id === props.selected} key={e.id}>{e.name}</Dropdown.Item>
            )}
        </Dropdown.Menu>
    </Dropdown>
}
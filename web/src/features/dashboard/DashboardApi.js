export async function fetchVessels() {
    return (await fetch("http://87.244.7.150:5000/vessels")).json();
}

export async function fetchVesselData(id) {
    return (await fetch(`http://87.244.7.150:5000/full_info?vessel_id=${id}`)).json();
}
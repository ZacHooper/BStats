import React from 'react';
import './ProfileBrawler.css'

const ProfileBrawler = (props) => {
    const handleImageSrc = (id) => {
        try {
            return require(`../../assets/brawlers/${id}.png`)
        } catch (error) {
            console.log(error)
        }
    }
    
    return (
        <div id={`brawler_${props.brawler.id}`} className="ProfileBrawler">
            <img alt={props.brawler.name} src={handleImageSrc(props.brawler.id)} width="180"></img>
            <h6>{props.brawler.name}</h6>
            <p>{props.brawler.trophies}</p>
        </div>
    );
}

export default ProfileBrawler;
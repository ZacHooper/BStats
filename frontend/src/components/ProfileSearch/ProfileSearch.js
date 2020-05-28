import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './ProfileSearch.css';

const ProfileSearch = (props) => {
    const [searchTag, setSearchTag] = useState("");
    
    const handleOnClick = () => {
        props.onClick(searchTag)
    }

    const handleOnChange = (e) => {
        setSearchTag(e.target.value);
    }
    
    return (
        <div className="ProfileSearch">
            <h1>Brawlstar Statistics</h1>
            <div className="ProfileSearch-input">
                <input type="text" onChange={handleOnChange} placeholder="Enter Player Tag..."></input>
                <Link to="/profile" onClick={handleOnClick}>Search</Link>
            </div>
            
        </div>
    )
}

export default ProfileSearch;
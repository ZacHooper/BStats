import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import './ProfileSearch.css';

const ProfileSearch = (props) => {
    const history = useHistory()

    const [searchTag, setSearchTag] = useState("");
    
    const handleOnClick = () => {
        props.onClick(searchTag)
        history.push("/profile");
    }

    const handleOnChange = (e) => {
        setSearchTag(e.target.value);
    }
    
    return (
        <div className="ProfileSearch">
            <h1>Brawlstar Statistics</h1>
            <div className="ProfileSearch-input">
                <input type="text" onChange={handleOnChange} placeholder="Enter Player Tag..."></input>
                <button onClick={handleOnClick}>Search</button>
            </div>
            
        </div>
    )
}

export default ProfileSearch;
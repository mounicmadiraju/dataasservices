import React, { Component } from 'react'

class JobForm extends Component {
    render () {
        return (
            <div>
                <form>
                    <input type="text" placeholder="job title, keywords etc"/>
                    <input type="text" max-length="5" placeholder="zip code"/>
                    <button>Search Jobs</button>
                </form>
            </div>
        )
    }
}

export default JobForm;
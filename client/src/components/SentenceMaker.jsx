import React from 'react';
import { RaisedButton, TextField } from 'material-ui'

class SentenceMaker extends React.PureComponent {
    renderInput() {
        return (
            <TextField fullWidth />
        )
    }
    renderButtons() {
        return (
            <div className="buttons" >
                <RaisedButton label="Find Sentiment" primary />
                <RaisedButton label="Reset" Secondary />
            </div>
        )
    }

    render() {
        return (
            <div className="sentence-maker">
                {this.renderInput()}
                {this.renderButtons()}
            </div>
        )
    }
}

export default SentenceMaker;
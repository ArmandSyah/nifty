import React from 'react';
import { RaisedButton, TextField } from 'material-ui'
import './SentenceMaker.css'

class SentenceMaker extends React.PureComponent {
    constructor(props) {
        super(props);
        this.state = {
            sentence: ''
        }
    }

    onChange = (e, newValue) => {
        this.setState({ sentence: newValue })
    }

    onReset = (e) => {
        this.setState({ sentence: '' })
    }

    renderInput() {
        const { sentence } = this.state;
        return (
            <TextField fullWidth hintText="Put any sentence you want here" value={sentence} onChange={this.onChange} />
        )
    }

    renderButtons() {
        return (
            <div className="buttons" >
                <RaisedButton label="Find Sentiment" primary />
                <RaisedButton label="Reset" secondary onClick={this.onReset} />
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
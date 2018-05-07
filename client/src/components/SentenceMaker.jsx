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

    onFind = (e) => {
        const { getSentiment } = this.props;
        const { sentence } = this.state;
        getSentiment(sentence);
        this.setState({ sentence: '' })
    }

    onReset = (e) => {
        const { reset } = this.props;
        reset();
        this.setState({ sentence: '' })
    }

    renderInput() {
        const { sentence } = this.state;
        return (
            <div className="text-field">
                <TextField fullWidth hintText="Put any sentence you want here" value={sentence} onChange={this.onChange} />
            </div>
        )
    }

    renderButtons() {
        return (
            <div className="buttons" >
                <RaisedButton label="Find Sentiment" primary onClick={this.onFind} />
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
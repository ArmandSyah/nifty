import React from 'react';
import { string } from 'prop-types'

class SentenceDisplay extends React.PureComponent {
    render() {
        const { sentence } = this.props;
        return (
            <h4>{sentence}</h4>
        )
    }
}

SentenceDisplay.defaultProps = {
    sentence: 'Write a sentence and see it\'s sentiment from 0 to 4'
}

SentenceDisplay.propTypes = {
    sentence: string
}

export default SentenceDisplay;
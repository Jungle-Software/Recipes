import { BASE_LOADING_MESSAGE } from '../../constants';
import { Loading } from './LoadingMessage.styles'

const LoadingMessage = () => {
    return (
          <Loading id="loading">{BASE_LOADING_MESSAGE}</Loading>
      );
}

export default LoadingMessage;
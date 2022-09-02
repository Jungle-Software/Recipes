import { BASE_ERROR_MESSAGE } from '../../constants';
import { Error } from './DevError.styles'

type Props = {
    message: string
}

const DevError = (props: Props) => {
    return (
          <Error id="error">{BASE_ERROR_MESSAGE}{props.message}</Error>
      );
}

export default DevError;
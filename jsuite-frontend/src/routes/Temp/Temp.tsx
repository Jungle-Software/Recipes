import {Global, Title} from './Temp.styles'
import {Outlet, Link} from 'react-router-dom';
import SharedTemp from '../../components/SharedTemp/SharedTemp';
import NavBar from '../../components/NavBar/NavBar';

const Temp = () => {
    return (
        <Global>
          <NavBar></NavBar>
          <Title>Welcome to JSuite!</Title>
          {/* Here goes the app's components */}
          <SharedTemp></SharedTemp>
        </Global>
      );
}

export default Temp;
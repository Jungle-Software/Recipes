import {Global, Title} from './Home.styles'
import NavBar from '../../components/NavBar/NavBar';

const Home = () => {
    return (
        <Global>
          <NavBar></NavBar>
          <Title>Welcome to JSuite!</Title>
          {/* Here goes the app's components */}
        </Global>
      );
}

export default Home;
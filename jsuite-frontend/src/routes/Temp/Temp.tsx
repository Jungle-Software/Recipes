import {Global, Title} from './Temp.styles'
import {Outlet, Link} from 'react-router-dom';

const Temp = () => {
    return (
        <Global>
          <Title>Welcome to JSuite!</Title>
          {/* Here goes the app's components */}
          <nav>
            <Link to="/invoices">Invoices</Link> {" "}
          </nav>
          <Outlet />
        </Global>
      );
}

export default Temp;
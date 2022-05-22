import { Global, Title } from "./Temp.styles";
import { useQuery, gql } from "@apollo/client";
import { getCookie } from "typescript-cookie";

const ALL_RECIPE_TITLE_QUERY = gql`
  {
    recipes {
      id
      title
    }
  }
`;

const Temp = () => {
  //const { data, loading, error } = useQuery(ALL_RECIPE_TITLE_QUERY);

  //if (loading) return <div>"Loading..."</div>;
  //if (error) return <pre>{error.message}</pre>;

  console.log(getCookie("csrftoken"));
  console.log("HIIIIIIIIIIIIII");


  return (
    <Global>
      <Title>Welcome to JSuite!</Title>
      {/* Here goes the app's components */}
      <ul>
        {/*data.recipes.map((recipe: any) => (
          <li key={recipe.id}>{recipe.title}</li>
        ))*/}
      </ul>
    </Global>
  );
};

export default Temp;

import { Global, Title } from "./Recipes.styles";
import { useQuery, gql } from "@apollo/client";
import { useState } from "react";
import DevError from "../../components/DevError/DevError";
import NavBar from "../../components/NavBar/NavBar";

import Selector from "./RecipeSelector/Selector";
import RecipeView from "./RecipeView/RecipeView";

export const ALL_RECIPES_QUERY = gql`
  query AllRecipes{
    allRecipes {
      id
      title
    }
  }
`;

const Recipes = () => {
  const [currentRecipeId, setCurrentRecipeId] = useState(0);
  const { data, loading, error } = useQuery(ALL_RECIPES_QUERY);

  if (loading) return <div>Loading...</div>;
  if (error) return <DevError />;

  return (
    <Global>
      <NavBar></NavBar>
      <Title>Recipes</Title>
      <Selector
        recipeIds={data.allRecipes}
        onRecipeChange={(recipeId: number) => setCurrentRecipeId(recipeId)}
      ></Selector>
      <RecipeView recipeId={currentRecipeId}></RecipeView>
    </Global>
  );
};

export default Recipes;

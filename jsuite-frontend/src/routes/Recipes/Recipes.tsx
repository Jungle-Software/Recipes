import { Global, Title } from "./Recipes.styles";
import { gql, useQuery } from "@apollo/client";
import { useState } from "react";
import DevError from "../../components/DevError/DevError";
import NavBar from "../../components/NavBar/NavBar";

import RecipeSelector from "./RecipeSelector/RecipeSelector";
import RecipeView from "./RecipeView/RecipeView";
import LoadingMessage from "../../components/LoadingMessage/LoadingMessage";

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
  const { data, loading, error, refetch } = useQuery(ALL_RECIPES_QUERY);

  if (loading) return <LoadingMessage />;
  if (error) return <DevError message={error.message}/>;

  const handleDelete = (recipeId: number) => {
    if (currentRecipeId == recipeId) {
      setCurrentRecipeId(0)
    }
    refetch()
  }

  return (
    <Global>
      <NavBar></NavBar>
      <Title>Recipes</Title>
      <RecipeSelector
        recipeIds={data.allRecipes}
        onRecipeSelect={(recipeId: number) => setCurrentRecipeId(recipeId)}
        onRecipeDelete={(recipeId: number) => handleDelete(recipeId)}
      ></RecipeSelector>
      <RecipeView recipeId={currentRecipeId}></RecipeView>
    </Global>
  );
};

export default Recipes;

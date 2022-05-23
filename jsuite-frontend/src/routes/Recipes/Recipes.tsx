import { Global, Title } from "./Recipes.styles";
import { useQuery, gql } from "@apollo/client";
import { useEffect, useState } from "react";

import Selector from "./components/Selector/Selector";
import RecipeView from "./components/View/RecipeView";

const ALL_RECIPE_TITLE_QUERY = gql`
  {
    recipes {
      id
      title
      description
      portionSize
      prepTime
      cookTime
      ingredients
      instructions
      additionalNotes
      nutritionalInfo
      dateCreated
    }
  }
`;

const Recipes = () => {
  const [currentRecipe, setCurrentRecipe] = useState();

  const { data, loading, error } = useQuery(ALL_RECIPE_TITLE_QUERY);

  if (loading) return <div>"Loading..."</div>;
  if (error) return <pre>{error.message}</pre>;

  return (
    <Global>
      <Title>Recipes</Title>
      <Selector
        recipes={data.recipes}
        onRecipeChange={(recipe: any) => setCurrentRecipe(recipe)}
      ></Selector>
      <RecipeView recipe={currentRecipe}></RecipeView>
    </Global>
  );
};

export default Recipes;

import { AddRecipeButton, Global, Title } from "./Recipes.styles";
import { gql, useQuery } from "@apollo/client";
import { useState } from "react";
import DevError from "../../components/DevError/DevError";
import NavBar from "../../components/NavBar/NavBar";

import RecipeSelector from "./RecipeSelector/RecipeSelector";
import RecipeView from "./RecipeView/RecipeView";
import LoadingMessage from "../../components/LoadingMessage/LoadingMessage";
import AddRecipeDialog from "./AddRecipeDialog/AddRecipeDialog";

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
  const [showAddRecipeDialog, setShowAddRecipeDialog] = useState(false);
  const { data, loading, error, refetch } = useQuery(ALL_RECIPES_QUERY);

  if (loading) return <LoadingMessage />;
  if (error) return <DevError message={error.message}/>;

  const handleAdd = () => {
    setShowAddRecipeDialog(false);
    refetch();
  }

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
      <AddRecipeButton onClick={() => {setShowAddRecipeDialog(true)}}>ADD RECIPE</AddRecipeButton>
      <AddRecipeDialog show={showAddRecipeDialog} hide={() => {setShowAddRecipeDialog(false)}} handleCreate={() => {handleAdd()}} />
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

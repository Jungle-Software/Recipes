import { useQuery, gql } from "@apollo/client";
import { View, Prompt } from "./RecipeView.styles";
import DevError from "../../../components/DevError/DevError";
import { SELECT_RECIPE_PROMPT } from "../../../constants";
import LoadingMessage from "../../../components/LoadingMessage/LoadingMessage";

export const RECIPE_BY_ID_QUERY = gql`
    query RecipeById($id: ID!) {
        recipeById(id: $id) {
            title
            description
            categories{
                name
            }
            servings
            prepTime
            cookTime
            instructions{
                title
                text
                subInstructions {
                    text
                }
            }
            ingredients{
                ingredient{
                    name
                    allergens{
                        type
                    }
                }
                unit
                quantity
            }
            additionalNotes
            dateUpdated
            dateCreated
        }
    }
`;

type Props = {
  recipeId: number
}

const RecipeView = (props: Props) => {
  const recipeId = props.recipeId;
  const { data, loading, error } = useQuery(RECIPE_BY_ID_QUERY, {
    variables: { id: recipeId },
  });

  if (recipeId === 0) return <Prompt id="select-recipe-prompt">{SELECT_RECIPE_PROMPT}</Prompt>;
  if (loading) return <LoadingMessage />;
  if (error) return <DevError message={error.message}/>;

  return (
    <View id="recipe-view">
      {data.recipeById.title}
      <br />
      {data.recipeById.description}
      <br />
      {data.recipeById.categories[0].name} {/*TEMPORARY FOR TESTING*/}
      <br />
      {data.recipeById.servings}
      <br />
      {data.recipeById.prepTime}
      <br />
      {data.recipeById.cookTime}
      <br />

        {data.recipeById.instructions[0].title}
        <br />
        {data.recipeById.instructions[0].text}
        <br />
        {data.recipeById.instructions[0].subInstructions[0].text} # TODO FIX CRASH WHEN TEXT IS NULL
        <br />

        {data.recipeById.ingredients[0].ingredient[0].name}
        <br/>
        {data.recipeById.ingredients[0].ingredient[0].allergens[0].type} # TODO FIX CRASH WHEN allergens is null
        <br/>
        {data.recipeById.ingredients[0].unit} {/*TEMPORARY FOR TESTING*/}
        <br />
        {data.recipeById.ingredients[0].quantity} {/*TEMPORARY FOR TESTING*/}
        <br />

      {data.recipeById.additionalNotes}
      <br />
      {data.recipeById.dateUpdated}
      <br />
      {data.recipeById.dateCreated}
    </View>
  );
};

export default RecipeView;
